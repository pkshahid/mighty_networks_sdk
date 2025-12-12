"""
Comments Resource

Handles all comment-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class CommentsResource(BaseResource):
    """
    Manage comments on posts.

    Comments are responses to posts within spaces.
    """

    def list(
        self,
        network_id: int,
        space_id: int,
        post_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List comments on a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of comments

        Example:
            >>> client.comments.list(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/comments"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def create(
        self,
        network_id: int,
        space_id: int,
        post_id: int,
        content: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a comment on a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID
            content: Comment content
            **kwargs: Additional comment properties

        Returns:
            Created comment details

        Example:
            >>> client.comments.create(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111,
            ...     content="Great post!"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/comments"
        data = {"content": content, **kwargs}
        return self._post(endpoint, json=data)

    def delete(
        self,
        network_id: int,
        space_id: int,
        post_id: int,
        comment_id: int
    ) -> Dict[str, Any]:
        """
        Delete a comment.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID
            comment_id: The comment ID

        Returns:
            Empty response on success

        Example:
            >>> client.comments.delete(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111,
            ...     comment_id=33333
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/comments/{comment_id}/"
        return self._delete(endpoint)
