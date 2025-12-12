"""
Basic Usage Examples for Mighty Networks SDK
"""
from mighty_networks_sdk import MightyNetworksClient

def main():
    # Initialize the client
    client = MightyNetworksClient(
        api_token="your_api_token_here"
    )
    
    network_id = 12345  # Replace with your network ID
    
    # Example 1: List all spaces
    print("=== Listing Spaces ===")
    spaces = client.spaces.list(network_id=network_id)
    for space in spaces['items']:
        print(f"Space: {space['name']} (ID: {space['id']})")
    
    # Example 2: Get space details
    if spaces['items']:
        space_id = spaces['items'][0]['id']
        print(f"\n=== Getting Space Details ===")
        space = client.spaces.get(network_id=network_id, space_id=space_id)
        print(f"Space Name: {space['name']}")
        print(f"Description: {space.get('description', 'N/A')}")
        
        # Example 3: List members in the space
        print(f"\n=== Listing Members in Space {space_id} ===")
        members = client.members.list(
            network_id=network_id,
            space_id=space_id,
            per_page=10
        )
        for member in members['items']:
            print(f"Member: {member['first_name']} {member['last_name']} ({member['email']})")
        
        # Example 4: List posts in the space
        print(f"\n=== Listing Posts in Space {space_id} ===")
        posts = client.posts.list(
            network_id=network_id,
            space_id=space_id,
            per_page=5
        )
        for post in posts['items']:
            print(f"Post: {post['title']}")
        
        # Example 5: List events in the space
        print(f"\n=== Listing Events in Space {space_id} ===")
        events = client.events.list(
            network_id=network_id,
            space_id=space_id,
            per_page=5
        )
        for event in events['items']:
            print(f"Event: {event['title']} - {event['start_time']}")

if __name__ == "__main__":
    main()
