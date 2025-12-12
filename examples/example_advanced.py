"""
Advanced Usage Examples for Mighty Networks SDK

This file demonstrates advanced features and patterns.
"""

from mighty_networks_sdk import MightyNetworksClient
from mighty_networks_sdk.exceptions import (
    RateLimitError,
    APIError
)
import time
from typing import List, Dict, Any


class MightyNetworksHelper:
    """
    Helper class with advanced utilities for Mighty Networks operations.
    """

    def __init__(self, api_token: str, network_id: int):
        self.client = MightyNetworksClient(api_token=api_token)
        self.network_id = network_id

    def get_all_paginated(
        self,
        resource_method,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Fetch all items from a paginated endpoint.

        Args:
            resource_method: The resource method to call
            **kwargs: Arguments to pass to the method

        Returns:
            List of all items across all pages
        """
        all_items = []
        page = 1

        while True:
            try:
                response = resource_method(
                    network_id=self.network_id,
                    page=page,
                    per_page=100,
                    **kwargs
                )

                items = response.get('items', [])
                all_items.extend(items)

                # Check if there's a next page
                if 'next' not in response.get('links', {}):
                    break

                page += 1
                time.sleep(0.1)  # Rate limiting

            except RateLimitError:
                print(f"Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                continue
            except APIError as e:
                print(f"API error: {e}")
                break

        return all_items

    def bulk_add_members(
        self,
        space_id: int,
        members_data: List[Dict[str, Any]],
        batch_size: int = 10
    ) -> Dict[str, List]:
        """
        Add multiple members to a space with batching and error handling.

        Args:
            space_id: The space ID
            members_data: List of member data dictionaries
            batch_size: Number of members to add before pausing

        Returns:
            Dictionary with 'success' and 'failed' lists
        """
        results = {'success': [], 'failed': []}

        for i, member_data in enumerate(members_data):
            try:
                result = self.client.members.add_to_space(
                    network_id=self.network_id,
                    space_id=space_id,
                    **member_data
                )
                results['success'].append(result)
                print(f"✓ Added: {member_data.get('email')}")

            except Exception as e:
                results['failed'].append({
                    'data': member_data,
                    'error': str(e)
                })
                print(f"✗ Failed: {member_data.get('email')} - {e}")

            # Batch pausing
            if (i + 1) % batch_size == 0:
                print(f"Processed {i + 1} members, pausing...")
                time.sleep(1)

        return results

    def sync_members_between_spaces(
        self,
        source_space_id: int,
        target_space_id: int,
        role: str = "member"
    ) -> int:
        """
        Sync members from one space to another.

        Args:
            source_space_id: Source space ID
            target_space_id: Target space ID
            role: Role to assign in target space

        Returns:
            Number of members synced
        """
        # Get all members from source space
        source_members = self.get_all_paginated(
            self.client.members.list,
            space_id=source_space_id
        )

        synced_count = 0

        for member in source_members:
            try:
                self.client.members.add_to_space(
                    network_id=self.network_id,
                    space_id=target_space_id,
                    email=member['email'],
                    first_name=member.get('first_name'),
                    last_name=member.get('last_name'),
                    role=role
                )
                synced_count += 1
                print(f"Synced: {member['email']}")

            except Exception as e:
                print(f"Failed to sync {member['email']}: {e}")

            time.sleep(0.2)  # Rate limiting

        return synced_count

    def get_engagement_stats(self, space_id: int) -> Dict[str, Any]:
        """
        Get engagement statistics for a space.

        Args:
            space_id: The space ID

        Returns:
            Dictionary with engagement statistics
        """
        # Get all posts
        posts = self.get_all_paginated(
            self.client.posts.list,
            space_id=space_id
        )

        # Get all members
        members = self.get_all_paginated(
            self.client.members.list,
            space_id=space_id
        )

        stats = {
            'total_members': len(members),
            'total_posts': len(posts),
            'average_posts_per_member': len(posts) / len(members) if members else 0,
            'posts_with_comments': sum(1 for p in posts if p.get('comment_count', 0) > 0),
            'total_comments': sum(p.get('comment_count', 0) for p in posts),
            'total_likes': sum(p.get('like_count', 0) for p in posts)
        }

        return stats


def main():
    """Main example runner."""
    api_token = "your_api_token_here"
    network_id = 12345
    space_id = 67890

    helper = MightyNetworksHelper(api_token, network_id)

    # Example 1: Get all members
    print("=== Fetching All Members ===")
    all_members = helper.get_all_paginated(
        helper.client.members.list,
        space_id=space_id
    )
    print(f"Total members: {len(all_members)}")

    # Example 2: Bulk add members
    print("\n=== Bulk Adding Members ===")
    new_members = [
        {"email": f"user{i}@example.com", "first_name": f"User{i}", "role": "member"}
        for i in range(1, 6)
    ]
    results = helper.bulk_add_members(space_id, new_members)
    print(f"Success: {len(results['success'])}, Failed: {len(results['failed'])}")

    # Example 3: Get engagement stats
    print("\n=== Engagement Statistics ===")
    stats = helper.get_engagement_stats(space_id)
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
