"""
Tags Resource

Handles all tag-related API operations.
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class TagsResource(BaseResource):
    """
    Manage tags for organizing content.

    Tags help categorize and organize posts and content.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all tags in a network.

        Args:
            network_id: The network ID

        Returns:
            List of tags

        Example:
            >>> client.tags.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/tags"
        params = {}
        return self._get(endpoint, params=params)

    def get(self, network_id: int, tag_id: int) -> Dict[str, Any]:
        """
        Get a specific tag by ID.

        Args:
            network_id: The network ID
            tag_id: The tag ID

        Returns:
            Tag details

        Example:
            >>> client.tags.get(network_id=12345, tag_id=555)
        """
        endpoint = f"/admin/v1/networks/{network_id}/tags/{tag_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new tag.

        Args:
            network_id: The network ID
            name: Tag name
            **kwargs: Additional tag properties

        Returns:
            Created tag details

        Example:
            >>> client.tags.create(
            ...     network_id=12345,
            ...     name="Announcements"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/tags"
        data = {"name": name, **kwargs}
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        tag_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a tag.

        Args:
            network_id: The network ID
            tag_id: The tag ID
            **kwargs: Tag properties to update

        Returns:
            Updated tag details

        Example:
            >>> client.tags.update(
            ...     network_id=12345,
            ...     tag_id=555,
            ...     name="Updated Tag Name"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/tags/{tag_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(self, network_id: int, tag_id: int) -> Dict[str, Any]:
        """
        Delete a tag.

        Args:
            network_id: The network ID
            tag_id: The tag ID

        Returns:
            Empty response on success

        Example:
            >>> client.tags.delete(network_id=12345, tag_id=555)
        """
        endpoint = f"/admin/v1/networks/{network_id}/tags/{tag_id}/"
        return self._delete(endpoint)
