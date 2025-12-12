"""
Error Handling Examples
"""
from mighty_networks_sdk import (
    MightyNetworksClient,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
    APIError
)

def main():
    client = MightyNetworksClient(api_token="your_api_token_here")
    
    # Example 1: Handle authentication errors
    try:
        invalid_client = MightyNetworksClient(api_token="invalid_token")
        spaces = invalid_client.spaces.list(network_id=12345)
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
    
    # Example 2: Handle resource not found
    try:
        space = client.spaces.get(network_id=12345, space_id=999999)
    except ResourceNotFoundError as e:
        print(f"Space not found: {e}")
    
    # Example 3: Handle validation errors
    try:
        new_space = client.spaces.create(
            network_id=12345,
            name="",  # Invalid: empty name
        )
    except ValidationError as e:
        print(f"Validation error: {e}")
    
    # Example 4: Handle rate limiting
    try:
        # Make many rapid requests
        for i in range(1000):
            client.spaces.list(network_id=12345)
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        print("Please wait before making more requests")
    
    # Example 5: Generic API error handling
    try:
        space = client.spaces.get(network_id=12345, space_id=67890)
    except APIError as e:
        print(f"API Error occurred: {e}")
        print(f"Status Code: {e.status_code}")
        print(f"Response: {e.response}")

if __name__ == "__main__":
    main()
