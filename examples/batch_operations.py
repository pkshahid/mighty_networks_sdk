"""
Batch Operations Examples
"""
from mighty_networks_sdk import MightyNetworksClient
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def add_members_batch(client, network_id, space_id, members_data):
    """
    Add multiple members to a space in batch.
    """
    results = []
    
    for member_data in members_data:
        try:
            result = client.members.add_to_space(
                network_id=network_id,
                space_id=space_id,
                **member_data
            )
            results.append(("success", result))
            print(f"✓ Added member: {member_data['email']}")
        except Exception as e:
            results.append(("error", str(e)))
            print(f"✗ Failed to add {member_data['email']}: {e}")
        
        # Rate limiting: small delay between requests
        time.sleep(0.5)
    
    return results

def main():
    client = MightyNetworksClient(api_token="your_api_token_here")
    
    network_id = 12345
    space_id = 67890
    
    # Example: Batch add members
    new_members = [
        {
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "role": "member"
        },
        {
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith",
            "role": "member"
        },
        {
            "email": "user3@example.com",
            "first_name": "Bob",
            "last_name": "Johnson",
            "role": "member"
        }
    ]
    
    print("=== Adding Members in Batch ===")
    results = add_members_batch(client, network_id, space_id, new_members)
    
    success_count = sum(1 for r in results if r[0] == "success")
    print(f"\nSuccessfully added {success_count}/{len(new_members)} members")

if __name__ == "__main__":
    main()
