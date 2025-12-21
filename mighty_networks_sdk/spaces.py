"""
Spaces Resource

Handles all space-related API operations.
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class SpacesResource(BaseResource):
    """
    Manage spaces within a network.

    Spaces are groups or communities within a Mighty Network.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all spaces in a network.

        Args:
            network_id: The network ID

        Returns:
            List of spaces

        Example:
            >>> client.spaces.list(network_id=12345)
            {
                "items": [...],
                "links": {"self": "...", "next": "..."}
            }
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces"
        params = {}
        return self._get(endpoint, params=params)

    def get(self, network_id: int, space_id: int) -> Dict[str, Any]:
        """
        Get a specific space by ID.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            Space details

        Example:
            >>> client.spaces.get(network_id=12345, space_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new space.

        Args:
            network_id: The network ID
            name: Space name
            **kwargs: Additional space properties

        Returns:
            Created space details

        Example:
            >>> client.spaces.create(
            ...     network_id=12345,
            ...     name="Developers Community",
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces"
        data = {
            "name": name,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        space_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a space.

        Args:
            network_id: The network ID
            space_id: The space ID
            **kwargs: Space properties to update

        Returns:
            Updated space details

        Example:
            >>> client.spaces.update(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     name="Updated Space Name"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}"
        return self._patch(endpoint, json=kwargs)

    def delete(self, network_id: int, space_id: int) -> Dict[str, Any]:
        """
        Delete a space.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            Empty response on success

        Example:
            >>> client.spaces.delete(network_id=12345, space_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}"
        return self._delete(endpoint)

    def list_members(
        self,
        network_id: int,
        space_id: int
    ) -> Dict[str, Any]:
        """
        List all members in a space.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            List of members

        Example:
            >>> client.spaces.list_members(network_id=12345,space_id=4333)
            {
                "items": [...],
                "links": {"self": "...", "next": "..."}
            }
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members"
        params = {}
        return self._get(endpoint, params=params)

    def add_member(
        self,
        network_id: int,
        space_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Add new user into space as a member

        Args:
            network_id: The network ID
            space_id: The Space ID
            user_id: The user ID of the user

        Returns:
            Added member details

        Example:
            >>> client.spaces.add_member(
            ...     network_id=12345,
            ...     space_id=12345,
            ...     user_id=12345,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members?user_id={user_id}"
        return self._post(endpoint)

    def get_member(self, network_id: int, space_id: int, member_id: int) -> Dict[str, Any]:
        """
        Get a specific member in the space by ID.

        Args:
            network_id: The network ID
            space_id: The space ID
            member_id: The Member ID

        Returns:
            Member details

        Example:
            >>> client.spaces.get_member(network_id=12345, space_id=67890, member_id=12331)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members/{member_id}"
        return self._get(endpoint)

    def update_member_role(
        self,
        network_id: int,
        space_id: int,
        member_id: int,
        role: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a member role in space.

        Args:
            network_id: The network ID
            space_id: The space ID
            member_id: The member ID
            role: New role
            **kwargs: Space member properties to update

        Returns:
            Updated space member details

        Example:
            >>> client.spaces.update_member_role(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     member_id=67890,
            ...     role="moderator"
            ... )
        """
        kwargs['role'] = role
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members/{member_id}"
        return self._put(endpoint, json=kwargs)

    def remove_member(self, network_id: int, space_id: int, member_id: int) -> Dict[str, Any]:
        """
        Remove member from the space.

        Args:
            network_id: The network ID
            space_id: The space ID
            member_id: The member ID

        Returns:
            Empty response on success

        Example:
            >>> client.spaces.remove_member(network_id=12345, space_id=67890, member_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/members/{member_id}"
        return self._delete(endpoint)