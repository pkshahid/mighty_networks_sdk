"""
Collections Resource

Handles all collection-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class CollectionsResource(BaseResource):
    """
    Manage content collections.

    Collections group related content together.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all collections in a network.

        Args:
            network_id: The network ID

        Returns:
            List of collections

        Example:
            >>> client.collections.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections"
        params = {}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        collection_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific collection by ID.

        Args:
            network_id: The network ID
            collection_id: The collection ID

        Returns:
            Collection details

        Example:
            >>> client.collections.get(
            ...     network_id=12345,
            ...     collection_id=666
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections/{collection_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        description: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new collection.

        Args:
            network_id: The network ID
            name: Collection name
            description: Collection description (optional)
            **kwargs: Additional collection properties

        Returns:
            Created collection details

        Example:
            >>> client.collections.create(
            ...     network_id=12345,
            ...     name="Getting Started",
            ...     description="Essential resources for new members"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections"
        data = {"name": name, **kwargs}
        if description:
            data["description"] = description

        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        collection_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a collection.

        Args:
            network_id: The network ID
            collection_id: The collection ID
            **kwargs: Collection properties to update

        Returns:
            Updated collection details

        Example:
            >>> client.collections.update(
            ...     network_id=12345,
            ...     collection_id=666,
            ...     name="Updated Collection Name"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections/{collection_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(
        self,
        network_id: int,
        collection_id: int
    ) -> Dict[str, Any]:
        """
        Delete a collection.

        Args:
            network_id: The network ID
            collection_id: The collection ID

        Returns:
            Empty response on success

        Example:
            >>> client.collections.delete(network_id=12345, collection_id=666)
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections/{collection_id}/"
        return self._delete(endpoint)

    def add_item(
        self,
        network_id: int,
        collection_id: int,
        item_type: str,
        item_id: int
    ) -> Dict[str, Any]:
        """
        Add an item to a collection.

        Args:
            network_id: The network ID
            collection_id: The collection ID
            item_type: Type of item (post, event, etc.)
            item_id: The item ID

        Returns:
            Updated collection details

        Example:
            >>> client.collections.add_item(
            ...     network_id=12345,
            ...     collection_id=666,
            ...     item_type="post",
            ...     item_id=11111
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections/{collection_id}/items"
        data = {"item_type": item_type, "item_id": item_id}
        return self._post(endpoint, json=data)

    def remove_item(
        self,
        network_id: int,
        collection_id: int,
        item_id: int
    ) -> Dict[str, Any]:
        """
        Remove an item from a collection.

        Args:
            network_id: The network ID
            collection_id: The collection ID
            item_id: The collection item ID

        Returns:
            Empty response on success

        Example:
            >>> client.collections.remove_item(
            ...     network_id=12345,
            ...     collection_id=666,
            ...     item_id=88888
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/collections/{collection_id}/items/{item_id}/"
        return self._delete(endpoint)
