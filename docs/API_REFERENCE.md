# API Reference

Complete reference for the Mighty Networks Python SDK.

## Table of Contents

- [Client](#client)
- [Resources](#resources)
  - [Spaces](#spaces)
  - [Members](#members)
  - [Posts](#posts)
  - [Events](#events)
  - [Plans](#plans)
  - [Custom Fields](#custom-fields)
  - [Comments](#comments)
  - [Tags](#tags)
  - [Polls](#polls)
  - [Subscriptions](#subscriptions)
  - [Purchases](#purchases)
  - [Invites](#invites)
  - [Collections](#collections)
  - [Badges](#badges)
  - [Assets](#assets)
  - [Abuse Reports](#abuse-reports)
- [Exceptions](#exceptions)
- [Models](#models)

## Client

### MightyNetworksClient

Main client for interacting with the Mighty Networks API.

```python
MightyNetworksClient(
    api_token: str,
    base_url: str = "https://api.mn.co",
    timeout: int = 30
)
```

**Parameters:**
- `api_token` (str, required): Your Mighty Networks API token
- `base_url` (str, optional): API base URL. Default: "https://api.mn.co"
- `timeout` (int, optional): Request timeout in seconds. Default: 30

**Example:**
```python
from mighty_networks_sdk import MightyNetworksClient

client = MightyNetworksClient(
    api_token="your_token_here",
    timeout=60
)
```

---

## Resources

### Spaces

Manage spaces (groups/communities) within your network.

#### list()

List all spaces in a network.

```python
client.spaces.list(
    network_id: int,
) -> Dict[str, Any]
```

#### get()

Get a specific space by ID.

```python
client.spaces.get(
    network_id: int,
    space_id: int
) -> Dict[str, Any]
```

#### create()

Create a new space.

```python
client.spaces.create(
    network_id: int,
    name: str,
    description: Optional[str] = None,
    is_public: bool = True,
    **kwargs
) -> Dict[str, Any]
```

#### update()

Update a space.

```python
client.spaces.update(
    network_id: int,
    space_id: int,
    **kwargs
) -> Dict[str, Any]
```

#### delete()

Delete a space.

```python
client.spaces.delete(
    network_id: int,
    space_id: int
) -> Dict[str, Any]
```

---

### Members

Manage members within spaces and networks.

#### list()

List members in a network or space.

```python
client.members.list(
    network_id: int,
    space_id: Optional[int] = None,
) -> Dict[str, Any]
```

#### get()

Get a specific member by ID.

```python
client.members.get(
    network_id: int,
    user_id: int,
    space_id: Optional[int] = None
) -> Dict[str, Any]
```

#### add_to_space()

Add a member to a space.

```python
client.members.add_to_space(
    network_id: int,
    space_id: int,
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    role: str = "member"
) -> Dict[str, Any]
```

#### update()

Update a member's information.

```python
client.members.update(
    network_id: int,
    user_id: int,
    space_id: Optional[int] = None,
    role: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]
```

#### remove()

Remove a member from a space.

```python
client.members.remove(
    network_id: int,
    user_id: int,
    space_id: int
) -> Dict[str, Any]
```

#### ban()

Ban a user from the network.

```python
client.members.ban(
    network_id: int,
    user_id: int,
    space_id: int,
    ban_reason: Optional[str] = None
) -> Dict[str, Any]
```

---

### Posts

Manage posts within spaces.

#### list()

List posts in a space.

```python
client.posts.list(
    network_id: int,
    space_id: int,
) -> Dict[str, Any]
```

#### get()

Get a specific post by ID.

```python
client.posts.get(
    network_id: int,
    space_id: int,
    post_id: int
) -> Dict[str, Any]
```

#### create()

Create a new post.

```python
client.posts.create(
    network_id: int,
    space_id: int,
    title: str,
    content: str,
    is_pinned: bool = False,
    **kwargs
) -> Dict[str, Any]
```

#### update()

Update a post.

```python
client.posts.update(
    network_id: int,
    space_id: int,
    post_id: int,
    **kwargs
) -> Dict[str, Any]
```

#### delete()

Delete a post.

```python
client.posts.delete(
    network_id: int,
    space_id: int,
    post_id: int
) -> Dict[str, Any]
```

#### pin()

Pin a post.

```python
client.posts.pin(
    network_id: int,
    space_id: int,
    post_id: int
) -> Dict[str, Any]
```

#### unpin()

Unpin a post.

```python
client.posts.unpin(
    network_id: int,
    space_id: int,
    post_id: int
) -> Dict[str, Any]
```

---

### Events

Manage events within spaces.

#### list()

List events in a space.

```python
client.events.list(
    network_id: int,
    space_id: int,
) -> Dict[str, Any]
```

#### get()

Get a specific event by ID.

```python
client.events.get(
    network_id: int,
    space_id: int,
    event_id: int
) -> Dict[str, Any]
```

#### create()

Create a new event.

```python
client.events.create(
    network_id: int,
    space_id: int,
    title: str,
    description: str,
    start_time: str,
    end_time: str,
    location: Optional[str] = None,
    is_online: bool = False,
    max_attendees: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]
```

#### update()

Update an event.

```python
client.events.update(
    network_id: int,
    space_id: int,
    event_id: int,
    **kwargs
) -> Dict[str, Any]
```

#### delete()

Delete an event.

```python
client.events.delete(
    network_id: int,
    space_id: int,
    event_id: int
) -> Dict[str, Any]
```

#### get_attendees()

Get event attendees.

```python
client.events.get_attendees(
    network_id: int,
    space_id: int,
    event_id: int,
) -> Dict[str, Any]
```

---

## Exceptions

### MightyNetworksException

Base exception for all SDK errors.

```python
from mighty_networks_sdk.exceptions import MightyNetworksException
```

### AuthenticationError

Raised when authentication fails.

```python
from mighty_networks_sdk.exceptions import AuthenticationError
```

### ResourceNotFoundError

Raised when a requested resource is not found (404).

```python
from mighty_networks_sdk.exceptions import ResourceNotFoundError
```

### ValidationError

Raised when request validation fails (422).

```python
from mighty_networks_sdk.exceptions import ValidationError
```

### RateLimitError

Raised when API rate limit is exceeded.

```python
from mighty_networks_sdk.exceptions import RateLimitError
```

### APIError

Raised for general API errors.

```python
from mighty_networks_sdk.exceptions import APIError

# Access error details
try:
    result = client.spaces.get(network_id=12345, space_id=67890)
except APIError as e:
    print(f"Status: {e.status_code}")
    print(f"Response: {e.response}")
```

---

## Models

### Member

```python
@dataclass
class Member:
    id: int
    email: str
    created_at: str
    updated_at: str
    permalink: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
```

### Space

```python
@dataclass
class Space:
    id: int
    name: str
    created_at: str
    updated_at: str
    permalink: Optional[str] = None
    description: Optional[str] = None
```

### Post

```python
@dataclass
class Post:
    id: int
    title: str
    content: str
    created_at: str
    updated_at: str
    author_id: int
    space_id: int
```

### Event

```python
@dataclass
class Event:
    id: int
    title: str
    description: str
    start_time: str
    end_time: str
    created_at: str
    updated_at: str
    space_id: int
```

---
