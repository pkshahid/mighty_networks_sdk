"""
Invites Resource

Handles all invitation-related API operations.
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class InvitesResource(BaseResource):
    """
    Manage member invitations.

    Invites allow you to invite new members to your network.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all invitations in a network.

        Args:
            network_id: The network ID

        Returns:
            List of invitations

        Example:
            >>> client.invites.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/invites"
        params = {}
        return self._get(endpoint, params=params)

    def create(
        self,
        network_id: int,
        emails: List[str],
        space_id: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create and send invitations.

        Args:
            network_id: The network ID
            emails: List of email addresses to invite
            space_id: Space to invite members to (optional)
            message: Custom invitation message (optional)
            **kwargs: Additional invitation properties

        Returns:
            Invitation details

        Example:
            >>> client.invites.create(
            ...     network_id=12345,
            ...     emails=["user1@example.com", "user2@example.com"],
            ...     space_id=67890,
            ...     message="Join our amazing community!"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/invites"
        data = {"emails": emails, **kwargs}
        if space_id:
            data["space_id"] = space_id
        if message:
            data["message"] = message

        return self._post(endpoint, json=data)

    def get(
        self,
        network_id: int,
        invite_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific invitation by ID.

        Args:
            network_id: The network ID
            invite_id: The invitation ID

        Returns:
            Invitation details

        Example:
            >>> client.invites.get(network_id=12345, invite_id=999)
        """
        endpoint = f"/admin/v1/networks/{network_id}/invites/{invite_id}/"
        return self._get(endpoint)

    def resend(
        self,
        network_id: int,
        invite_id: int
    ) -> Dict[str, Any]:
        """
        Resend an invitation.

        Args:
            network_id: The network ID
            invite_id: The invitation ID

        Returns:
            Updated invitation details

        Example:
            >>> client.invites.resend(network_id=12345, invite_id=999)
        """
        endpoint = f"/admin/v1/networks/{network_id}/invites/{invite_id}/resend"
        return self._post(endpoint)

    def revoke(
        self,
        network_id: int,
        invite_id: int
    ) -> Dict[str, Any]:
        """
        Revoke an invitation.

        Args:
            network_id: The network ID
            invite_id: The invitation ID

        Returns:
            Empty response on success

        Example:
            >>> client.invites.revoke(network_id=12345, invite_id=999)
        """
        endpoint = f"/admin/v1/networks/{network_id}/invites/{invite_id}/"
        return self._delete(endpoint)
