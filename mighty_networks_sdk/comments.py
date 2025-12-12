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
        post_id: int
    ) -> Dict[str, Any]:
        """
        List comments on a post.

        Args:
            network_id: The network ID
            space_id: The space ID
            post_id: The post ID

        Returns:
            List of comments

        Example:
            >>> client.comments.list(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     post_id=11111
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/comments"
        params = {}
        return self._get(endpoint, params=params)

    def create(self, network_id: int, post_id: int, text: str, reply_to_id: int = None):
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/comments"
        data = {"text": text}
        if reply_to_id:
            data["reply_to_id"] = reply_to_id
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
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/posts/{post_id}/comments/{comment_id}/"
        return self._delete(endpoint)
