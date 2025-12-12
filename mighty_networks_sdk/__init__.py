"""
Mighty Networks SDK

A production-ready Python SDK for the Mighty Networks API.

This SDK provides a simple, intuitive interface for interacting with
Mighty Networks API v1, with full support for all API endpoints.

Example:
    >>> from mighty_networks_sdk import MightyNetworksClient
    >>> 
    >>> client = MightyNetworksClient(api_token="your_api_token_here")
    >>> spaces = client.spaces.list(network_id=12345)
    >>> members = client.members.list(network_id=12345, space_id=67890)

For full documentation, visit: https://github.com/yourusername/mighty-networks-sdk
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

from .client import MightyNetworksClient
from .exceptions import (
    MightyNetworksException,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
    APIError
)
from .models import (
    Member,
    Space,
    Post,
    Event,
    Plan,
    CustomField,
    Badge
)

__all__ = [
    # Main client
    'MightyNetworksClient',

    # Exceptions
    'MightyNetworksException',
    'AuthenticationError',
    'ResourceNotFoundError',
    'ValidationError',
    'RateLimitError',
    'APIError',

    # Models
    'Member',
    'Space',
    'Post',
    'Event',
    'Plan',
    'CustomField',
    'Badge',
]
