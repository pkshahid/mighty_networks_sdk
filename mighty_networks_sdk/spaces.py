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
        description: Optional[str] = None,
        is_public: bool = True,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new space.

        Args:
            network_id: The network ID
            name: Space name
            description: Space description (optional)
            is_public: Whether the space is public (default: True)
            **kwargs: Additional space properties

        Returns:
            Created space details

        Example:
            >>> client.spaces.create(
            ...     network_id=12345,
            ...     name="Developers Community",
            ...     description="A space for developers"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces"
        data = {
            "name": name,
            "description": description,
            "is_public": is_public,
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
