"""
Mighty Networks SDK Client

The main client class for interacting with the Mighty Networks API.
"""

from typing import Optional
from .spaces import SpacesResource
from .members import MembersResource
from .posts import PostsResource
from .events import EventsResource
from .plans import PlansResource
from .custom_fields import CustomFieldsResource
from .comments import CommentsResource
from .tags import TagsResource
from .subscriptions import SubscriptionsResource
from .purchases import PurchasesResource
from .polls import PollsResource
from .invites import InvitesResource
from .collections import CollectionsResource
from .badges import BadgesResource
from .assets import AssetsResource
from .abuse_reports import AbuseReportsResource
from .me import MeResource
from .network import NetworkResource


class MightyNetworksClient:
    """
    Main client for interacting with the Mighty Networks API.

    This client provides access to all API resources including spaces,
    members, posts, events, plans, and more.

    Attributes:
        api_token: Your Mighty Networks API token
        base_url: The API base URL (default: https://api.mn.co)
        timeout: Request timeout in seconds (default: 30)
        spaces: Access to spaces resource
        members: Access to members resource
        posts: Access to posts resource
        events: Access to events resource
        plans: Access to plans resource
        custom_fields: Access to custom fields resource
        comments: Access to comments resource
        tags: Access to tags resource
        subscriptions: Access to subscriptions resource
        purchases: Access to purchases resource
        polls: Access to polls resource
        invites: Access to invites resource
        collections: Access to collections resource
        badges: Access to badges resource
        assets: Access to assets resource
        abuse_reports: Access to abuse reports resource
        me: Access to current authenticated user details
        network: Access to network details

    Example:
        >>> from mighty_networks_sdk import MightyNetworksClient
        >>> 
        >>> # Initialize the client
        >>> client = MightyNetworksClient(api_token="your_api_token_here")
        >>> 
        >>> # Use the client to interact with the API
        >>> spaces = client.spaces.list(network_id=12345)
        >>> members = client.members.list(network_id=12345, space_id=67890)
        >>> plans = client.plans.list(network_id=12345)
    """

    def __init__(
        self,
        api_token: str,
        base_url: str = "https://api.mn.co",
        timeout: int = 30
    ):
        """
        Initialize the Mighty Networks client.

        Args:
            api_token: Your Mighty Networks API token (required)
            base_url: The API base URL (default: https://api.mn.co)
            timeout: Request timeout in seconds (default: 30)

        Raises:
            ValueError: If api_token is not provided

        Example:
            >>> client = MightyNetworksClient(
            ...     api_token="your_api_token_here",
            ...     timeout=60
            ... )
        """
        if not api_token:
            raise ValueError("API token is required")

        self.api_token = api_token
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

        # Initialize all resource instances
        self.spaces = SpacesResource(self)
        self.members = MembersResource(self)
        self.posts = PostsResource(self)
        self.events = EventsResource(self)
        self.plans = PlansResource(self)
        self.custom_fields = CustomFieldsResource(self)
        self.comments = CommentsResource(self)
        self.tags = TagsResource(self)
        self.subscriptions = SubscriptionsResource(self)
        self.purchases = PurchasesResource(self)
        self.polls = PollsResource(self)
        self.invites = InvitesResource(self)
        self.collections = CollectionsResource(self)
        self.badges = BadgesResource(self)
        self.assets = AssetsResource(self)
        self.abuse_reports = AbuseReportsResource(self)
        self.me = MeResource(self)
        self.network = NetworkResource(self)

    def __repr__(self) -> str:
        """Return string representation of the client."""
        return f"MightyNetworksClient(base_url='{self.base_url}')"
