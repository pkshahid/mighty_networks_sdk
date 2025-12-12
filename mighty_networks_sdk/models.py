"""
Mighty Networks SDK Models

Data models for API request and response objects.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class Member:
    """Represents a network member."""
    id: int
    email: str
    created_at: str
    updated_at: str
    permalink: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    time_zone: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    referral_count: Optional[int] = None
    avatar: Optional[str] = None
    categories: Optional[str] = None
    ambassador_level: Optional[str] = None


@dataclass
class Space:
    """Represents a space within a network."""
    id: int
    name: str
    created_at: str
    updated_at: str
    permalink: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None
    member_count: Optional[int] = None


@dataclass
class Post:
    """Represents a post in a space."""
    id: int
    title: str
    content: str
    created_at: str
    updated_at: str
    author_id: int
    space_id: int
    permalink: Optional[str] = None
    comment_count: Optional[int] = None
    like_count: Optional[int] = None
    is_pinned: Optional[bool] = None


@dataclass
class Event:
    """Represents an event."""
    id: int
    title: str
    description: str
    start_time: str
    end_time: str
    created_at: str
    updated_at: str
    space_id: int
    location: Optional[str] = None
    is_online: Optional[bool] = None
    max_attendees: Optional[int] = None


@dataclass
class Plan:
    """Represents a membership plan."""
    id: int
    name: str
    description: str
    price: float
    currency: str
    interval: str
    created_at: str
    updated_at: str
    is_active: Optional[bool] = None
    trial_days: Optional[int] = None


@dataclass
class PaginatedResponse:
    """Represents a paginated API response."""
    items: List[Dict[str, Any]]
    links: Dict[str, str]

    @property
    def has_next(self) -> bool:
        """Check if there is a next page."""
        return 'next' in self.links

    @property
    def next_url(self) -> Optional[str]:
        """Get the URL for the next page."""
        return self.links.get('next')


@dataclass
class CustomField:
    """Represents a custom field."""
    id: int
    name: str
    field_type: str
    required: bool
    created_at: str
    updated_at: str
    options: Optional[List[str]] = None


@dataclass
class Badge:
    """Represents a badge."""
    id: int
    name: str
    description: str
    image_url: str
    created_at: str
    updated_at: str
