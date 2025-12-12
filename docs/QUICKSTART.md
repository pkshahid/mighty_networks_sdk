# Quick Start Guide

Get started with the Mighty Networks Python SDK in minutes.

## Installation

```bash
pip install mighty-networks-sdk
```

## Authentication

Get your API token from your Mighty Network's admin settings.

```python
from mighty_networks_sdk import MightyNetworksClient

client = MightyNetworksClient(api_token="your_api_token_here")
```

## Basic Usage

### 1. List All Spaces

```python
# Get all spaces in your network
spaces = client.spaces.list(network_id=12345)

for space in spaces['items']:
    print(f"Space: {space['name']} (ID: {space['id']})")
```

### 2. Get Space Details

```python
# Get details for a specific space
space = client.spaces.get(network_id=12345, space_id=67890)
print(f"Space Name: {space['name']}")
print(f"Description: {space['description']}")
print(f"Members: {space['member_count']}")
```

### 3. List Members

```python
# List all members in a space
members = client.members.list(
    network_id=12345,
    space_id=67890,
    per_page=50
)

for member in members['items']:
    print(f"{member['first_name']} {member['last_name']} - {member['email']}")
```

### 4. Add a New Member

```python
# Add a member to a space
new_member = client.members.add_to_space(
    network_id=12345,
    space_id=67890,
    email="newmember@example.com",
    first_name="Jane",
    last_name="Doe",
    role="member"
)

print(f"Added member: {new_member['email']}")
```

### 5. Create a Post

```python
# Create a new post in a space
post = client.posts.create(
    network_id=12345,
    space_id=67890,
    title="Welcome to the Community!",
    content="Hello everyone! Excited to be here and connect with all of you.",
    is_pinned=True
)

print(f"Created post: {post['title']}")
```

### 6. Create an Event

```python
# Create a new event
event = client.events.create(
    network_id=12345,
    space_id=67890,
    title="Community Meetup",
    description="Join us for our monthly community meetup!",
    start_time="2024-03-01T18:00:00Z",
    end_time="2024-03-01T20:00:00Z",
    location="San Francisco, CA",
    max_attendees=50
)

print(f"Created event: {event['title']}")
```

## Error Handling

Always handle potential errors:

```python
from mighty_networks_sdk.exceptions import (
    AuthenticationError,
    ResourceNotFoundError,
    APIError
)

try:
    space = client.spaces.get(network_id=12345, space_id=67890)
    print(f"Found space: {space['name']}")

except AuthenticationError:
    print("Invalid API token")

except ResourceNotFoundError:
    print("Space not found")

except APIError as e:
    print(f"API error: {e}")
```

## Pagination

Handle paginated results:

```python
# Method 1: Manual pagination
page = 1
while True:
    response = client.members.list(
        network_id=12345,
        space_id=67890,
        page=page,
        per_page=100
    )

    # Process members
    for member in response['items']:
        print(member['email'])

    # Check for next page
    if 'next' not in response['links']:
        break

    page += 1

# Method 2: Helper function
def get_all_members(client, network_id, space_id):
    all_members = []
    page = 1

    while True:
        response = client.members.list(
            network_id=network_id,
            space_id=space_id,
            page=page,
            per_page=100
        )

        all_members.extend(response['items'])

        if 'next' not in response['links']:
            break

        page += 1

    return all_members

# Use it
members = get_all_members(client, 12345, 67890)
print(f"Total members: {len(members)}")
```

## Next Steps

- Read the [API Reference](api_reference.md) for complete documentation
- Check out [Examples](../examples/) for more use cases
- Learn about [Advanced Usage](advanced_usage.md)

## Common Patterns

### Update Member Role

```python
# Update a member's role to moderator
client.members.update(
    network_id=12345,
    user_id=99999,
    space_id=67890,
    role="moderator"
)
```

### Pin/Unpin Posts

```python
# Pin a post
client.posts.pin(
    network_id=12345,
    space_id=67890,
    post_id=11111
)

# Unpin a post
client.posts.unpin(
    network_id=12345,
    space_id=67890,
    post_id=11111
)
```

### Get Event Attendees

```python
# Get all attendees for an event
attendees = client.events.get_attendees(
    network_id=12345,
    space_id=67890,
    event_id=22222
)

for attendee in attendees['items']:
    print(f"{attendee['first_name']} {attendee['last_name']}")
```

## Support

- 📖 [Full Documentation](https://github.com/yourusername/mighty-networks-sdk)
- 🐛 [Report Issues](https://github.com/yourusername/mighty-networks-sdk/issues)
- 💬 [Discussions](https://github.com/yourusername/mighty-networks-sdk/discussions)
