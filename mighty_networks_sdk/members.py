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
        space_id: Optional[int] = None,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List members in a network or space.

        Args:
            network_id: The network ID
            space_id: The space ID (optional, lists network members if not provided)
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of members

        Example:
            >>> # List all network members
            >>> client.members.list(network_id=12345)

            >>> # List space members
            >>> client.members.list(network_id=12345, space_id=67890)
        """
        if space_id:
            endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members"
        else:
            endpoint = f"admin/v1/networks/{network_id}/members"

        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        user_id: int,
        space_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get a specific member by ID.

        Args:
            network_id: The network ID
            user_id: The user ID
            space_id: The space ID (optional)

        Returns:
            Member details

        Example:
            >>> client.members.get(
            ...     network_id=12345,
            ...     user_id=99999,
            ...     space_id=67890
            ... )
        """
        if space_id:
            endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members/{user_id}/"
        else:
            endpoint = f"admin/v1/networks/{network_id}/members/{user_id}/"

        return self._get(endpoint)

    def update(
        self,
        network_id: int,
        user_id: int,
        space_id: Optional[int] = None,
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
            space_id: The space ID (optional)
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
            ...     space_id=67890,
            ...     role="moderator",
            ...     first_name="John"
            ... )
        """
        if space_id:
            endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members/{user_id}/"
        else:
            endpoint = f"admin/v1/networks/{network_id}/members/{user_id}/"

        data = {k: v for k, v in {
            "role": role,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            **kwargs
        }.items() if v is not None}

        return self._patch(endpoint, json=data)

    def remove(
        self,
        network_id: int,
        user_id: int,
        space_id: int
    ) -> Dict[str, Any]:
        """
        Remove a member from a space.

        Args:
            network_id: The network ID
            user_id: The user ID
            space_id: The space ID

        Returns:
            Empty response on success

        Example:
            >>> client.members.remove(
            ...     network_id=12345,
            ...     user_id=99999,
            ...     space_id=67890
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members/{user_id}/"
        return self._delete(endpoint)

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
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members/{user_id}/ban"
        data = {}
        if ban_reason:
            data["ban_reason"] = ban_reason
        return self._post(endpoint, json=data)

    def add_to_space(
        self,
        network_id: int,
        space_id: int,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        role: str = "member"
    ) -> Dict[str, Any]:
        """
        Add a member to a space.

        Args:
            network_id: The network ID
            space_id: The space ID
            email: Member email
            first_name: Member first name (optional)
            last_name: Member last name (optional)
            role: Member role (default: "member")

        Returns:
            Created member details

        Example:
            >>> client.members.add_to_space(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     email="newmember@example.com",
            ...     first_name="Jane",
            ...     role="member"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/members"
        data = {
            "email": email,
            "role": role
        }
        if first_name:
            data["first_name"] = first_name
        if last_name:
            data["last_name"] = last_name

        return self._post(endpoint, json=data)
