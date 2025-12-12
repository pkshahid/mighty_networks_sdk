"""
Pagination Examples
"""
from mighty_networks_sdk import MightyNetworksClient

def fetch_all_members(client, network_id, space_id):
    """
    Fetch all members from a space using pagination.
    """
    all_members = []
    page = 1
    
    print(f"Fetching members from space {space_id}...")
    
    while True:
        response = client.members.list(
            network_id=network_id,
            space_id=space_id,
            page=page,
            per_page=100  # Maximum allowed per page
        )
        
        members = response['items']
        all_members.extend(members)
        
        print(f"Page {page}: Fetched {len(members)} members")
        
        # Check if there's a next page
        if 'next' not in response['links']:
            break
        
        page += 1
    
    return all_members

def main():
    client = MightyNetworksClient(api_token="your_api_token_here")
    
    network_id = 12345
    space_id = 67890
    
    # Fetch all members
    all_members = fetch_all_members(client, network_id, space_id)
    
    print(f"\nTotal members fetched: {len(all_members)}")
    
    # Process the members
    for i, member in enumerate(all_members[:10], 1):
        print(f"{i}. {member['first_name']} {member['last_name']} - {member['email']}")

if __name__ == "__main__":
    main()
