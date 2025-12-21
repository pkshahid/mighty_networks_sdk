"""
Members Resource

Handles all member-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class MembersResource(BaseResource):
    """
    Manage members within spaces and networks.

    Members are users who belong to spaces and networks.
    """

    def list(
        self,
        network_id: int,
    ) -> Dict[str, Any]:
        """
        List members in a network.

        Args:
            network_id: The network ID

        Returns:
            List of members

        Example:
            >>> # List all network members
            >>> client.members.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/members"

        params = {}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Get a specific member by ID.

        Args:
            network_id: The network ID
            user_id: The user ID

        Returns:
            Member details

        Example:
            >>> client.members.get(
            ...     network_id=12345,
            ...     user_id=99999,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/"

        return self._get(endpoint)

    def get_by_email(
        self,
        network_id: int,
        email: str,
    ) -> Dict[str, Any]:
        """
        Get a specific member by email.

        Args:
            network_id: The network ID
            email: The user email

        Returns:
            Member details

        Example:
            >>> client.members.get(
            ...     network_id=12345,
            ...     email=john@mail.com,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/by_email?email={email}"

        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        email: str,
        first_name: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new space.

        Args:
            network_id: The network ID
            email: Email of the member
            first_name: First name of the member
            **kwargs: Additional member properties (last_name, role)

        Returns:
            Created space member

        Example:
            >>> client.members.create(
            ...     network_id=12345,
            ...     email="john@mail.com",
            ...     first_name="John",
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members"
        data = {
            "first_name": first_name,
            "email": email,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def soft_delete(
        self,
        network_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Soft delete a member account

        Args:
            network_id: The network ID
            user_id: The member ID

        Returns:
            empty reponse on success

        Example:
            >>> client.members.soft_delete(
            ...     network_id=12345,
            ...     user_id=23434,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/"

        return self._delete(endpoint)

    def delete(
        self,
        network_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Delete a member account from the network

        Args:
            network_id: The network ID
            user_id: The member ID

        Returns:
            empty reponse on success

        Example:
            >>> client.members.delete(
            ...     network_id=12345,
            ...     user_id=23434,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/network_membership"

        return self._delete(endpoint,)

    def update(
        self,
        network_id: int,
        user_id: int,
        role: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a member's information.

        Args:
            network_id: The network ID
            user_id: The user ID
            role: Member role (e.g., "member", "moderator", "admin")
            email: Member email
            first_name: Member first name
            last_name: Member last name
            **kwargs: Additional member properties

        Returns:
            Updated member details

        Example:
            >>> client.members.update(
            ...     network_id=12345,
            ...     user_id=99999,
            ...     role="moderator",
            ...     first_name="John"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/"

        data = {k: v for k, v in {
            "role": role,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            **kwargs
        }.items() if v is not None}

        return self._patch(endpoint, json=data)

    def ban(
        self,
        network_id: int,
        user_id: int,
        space_id: int,
        ban_reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Ban a user from the network.

        Args:
            network_id: The network ID
            user_id: The user ID to ban
            space_id: The space ID
            ban_reason: Reason for banning (optional)

        Returns:
            Empty response on success

        Example:
            >>> client.members.ban(
            ...     network_id=12345,
            ...     user_id=99999,
            ...     space_id=67890,
            ...     ban_reason="Violation of community guidelines"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members/{user_id}/ban"
        data = {}
        if ban_reason:
            data["ban_reason"] = ban_reason
        return self._post(endpoint, json=data)
