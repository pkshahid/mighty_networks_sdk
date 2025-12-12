"""
Data Export Examples

Export data from Mighty Networks for backup or analysis.
"""

from mighty_networks_sdk import MightyNetworksClient
import csv
import json
from datetime import datetime


class MightyNetworksExporter:
    """Export data from Mighty Networks."""

    def __init__(self, api_token: str, network_id: int):
        self.client = MightyNetworksClient(api_token=api_token)
        self.network_id = network_id

    def export_members_to_csv(
        self,
        space_id: int,
        filename: str = None
    ) -> str:
        """
        Export all members to a CSV file.

        Args:
            space_id: The space ID
            filename: Output filename (optional)

        Returns:
            Path to the exported file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"members_export_{timestamp}.csv"

        members = []
        page = 1

        # Fetch all members
        while True:
            response = self.client.members.list(
                network_id=self.network_id,
                space_id=space_id,
                page=page,
                per_page=100
            )

            members.extend(response['items'])

            if 'next' not in response['links']:
                break

            page += 1

        # Write to CSV
        if members:
            fieldnames = members[0].keys()

            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(members)

        print(f"Exported {len(members)} members to {filename}")
        return filename

    def export_posts_to_json(
        self,
        space_id: int,
        filename: str = None,
        include_comments: bool = False
    ) -> str:
        """
        Export all posts to a JSON file.

        Args:
            space_id: The space ID
            filename: Output filename (optional)
            include_comments: Whether to include comments

        Returns:
            Path to the exported file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"posts_export_{timestamp}.json"

        posts = []
        page = 1

        # Fetch all posts
        while True:
            response = self.client.posts.list(
                network_id=self.network_id,
                space_id=space_id,
                page=page,
                per_page=100
            )

            for post in response['items']:
                post_data = post.copy()

                # Optionally include comments
                if include_comments:
                    comments = self.client.comments.list(
                        network_id=self.network_id,
                        space_id=space_id,
                        post_id=post['id']
                    )
                    post_data['comments'] = comments.get('items', [])

                posts.append(post_data)

            if 'next' not in response['links']:
                break

            page += 1

        # Write to JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)

        print(f"Exported {len(posts)} posts to {filename}")
        return filename

    def export_space_summary(
        self,
        space_id: int,
        filename: str = None
    ) -> str:
        """
        Export a comprehensive summary of a space.

        Args:
            space_id: The space ID
            filename: Output filename (optional)

        Returns:
            Path to the exported file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"space_summary_{timestamp}.json"

        # Get space details
        space = self.client.spaces.get(
            network_id=self.network_id,
            space_id=space_id
        )

        # Get counts
        members = self.client.members.list(
            network_id=self.network_id,
            space_id=space_id,
            per_page=1
        )

        posts = self.client.posts.list(
            network_id=self.network_id,
            space_id=space_id,
            per_page=1
        )

        events = self.client.events.list(
            network_id=self.network_id,
            space_id=space_id,
            per_page=1
        )

        summary = {
            'space': space,
            'statistics': {
                'member_count': len(members.get('items', [])),
                'post_count': len(posts.get('items', [])),
                'event_count': len(events.get('items', [])),
            },
            'exported_at': datetime.now().isoformat()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print(f"Exported space summary to {filename}")
        return filename


def main():
    """Main example runner."""
    api_token = "your_api_token_here"
    network_id = 12345
    space_id = 67890

    exporter = MightyNetworksExporter(api_token, network_id)

    # Export members
    print("=== Exporting Members ===")
    exporter.export_members_to_csv(space_id)

    # Export posts
    print("\n=== Exporting Posts ===")
    exporter.export_posts_to_json(space_id, include_comments=True)

    # Export space summary
    print("\n=== Exporting Space Summary ===")
    exporter.export_space_summary(space_id)


if __name__ == "__main__":
    main()
