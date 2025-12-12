"""
Posts Resource

Handles all post-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class PostsResource(BaseResource):
    """
    Manage posts within spaces.

    Posts are content items created by members in spaces.
    """

    def list(
        self,
        network_id: int,
        space_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List posts in a space.

        Args:
            network_id: The network ID
            space_id: The space ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of posts

        Example:
            >>> client.posts.list(network_id=12345, space_id=67890)
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        space_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific post by ID.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID

        Returns:
            Post details

        Example:
            >>> client.posts.get(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        space_id: int,
        title: str,
        content: str,
        is_pinned: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new post.

        Args:
            network_id: The network ID
            space_id: The space ID
            title: Post title
            content: Post content
            is_pinned: Whether to pin the post (default: False)
            **kwargs: Additional post properties

        Returns:
            Created post details

        Example:
            >>> client.posts.create(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     title="Welcome to the Community!",
            ...     content="Hello everyone, excited to be here.",
            ...     is_pinned=True
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts"
        data = {
            "title": title,
            "content": content,
            "is_pinned": is_pinned,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        space_id: int,
        post_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID
            **kwargs: Post properties to update

        Returns:
            Updated post details

        Example:
            >>> client.posts.update(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111,
            ...     title="Updated Title"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(
        self,
        network_id: int,
        space_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Delete a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID

        Returns:
            Empty response on success

        Example:
            >>> client.posts.delete(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/"
        return self._delete(endpoint)

    def pin(
        self,
        network_id: int,
        space_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Pin a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID

        Returns:
            Updated post details

        Example:
            >>> client.posts.pin(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/pin"
        return self._post(endpoint)

    def unpin(
        self,
        network_id: int,
        space_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Unpin a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID

        Returns:
            Updated post details

        Example:
            >>> client.posts.unpin(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/unpin"
        return self._post(endpoint)
