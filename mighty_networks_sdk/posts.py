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
        space_id: int
    ) -> Dict[str, Any]:
        """
        List posts in a space.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            List of posts

        Example:
            >>> client.posts.list(network_id=12345, space_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts"
        params = {
            'space_id' : space_id
        }
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific post by ID.

        Args:
            network_id: The network ID
            post_id: The post ID

        Returns:
            Post details

        Example:
            >>> client.posts.get(
            ...     network_id=12345,
            ...     post_id=11111
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        space_id: int,
        title: str,
        description: str,
        post_type: str,
        notify: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new post.

        Args:
            network_id: The network ID
            space_id: The space ID
            title: Post title
            description: Post description
            post_type: Post type
            notify : Should notify about post?
            **kwargs: Additional post properties

        Returns:
            Created post details

        Example:
            >>> client.posts.create(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     title="Welcome to the Community!",
            ...     description="Hello everyone, excited to be here.",
            ...     is_pinned=True
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts"
        if notify:
            endpoint += "?notify=true"
        data = {
            "title": title,
            "description": description,
            "post_type": post_type,
            "space_id" : space_id,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        post_id: int,
        notify: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a post.

        Args:
            network_id: The network ID
            post_id: The post ID
            notify: Should notify?
            **kwargs: Post properties to update

        Returns:
            Updated post details

        Example:
            >>> client.posts.update(
            ...     network_id=12345,
            ...     post_id=11111,
            ...     title="Updated Title",
            ...     description="Updated description"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/"
        if notify:
            endpoint += "?notify=true"
        return self._patch(endpoint, json=kwargs)

    def delete(
        self,
        network_id: int,
        post_id: int
    ) -> Dict[str, Any]:
        """
        Delete a post.

        Args:
            network_id: The network ID
            post_id: The post ID

        Returns:
            Empty response on success

        Example:
            >>> client.posts.delete(
            ...     network_id=12345,
            ...     post_id=11111
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/"
        return self._delete(endpoint)


    def mute(
        self,
        network_id: int,
        post_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Mute a post for a specific user (unfollow notifications).

        Args:
            network_id: The network ID
            post_id: The post ID
            user_id: The user ID

        Returns:
            Post successfully muted for the user

        Example:
            >>> client.posts.mute(
            ...     network_id=12345,
            ...     post_id=67890,
            ...     user_id=23423423,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/mute?user_id={user_id}"
        return self._post(endpoint)

    def unmute(
        self,
        network_id: int,
        post_id: int,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Unute a post for a specific user.

        Args:
            network_id: The network ID
            post_id: The post ID
            user_id: The user ID

        Returns:
            Post successfully unmuted for the user

        Example:
            >>> client.posts.unmute(
            ...     network_id=12345,
            ...     post_id=67890,
            ...     user_id=23423423,
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/posts/{post_id}/mute?user_id={user_id}"
        return self._delete(endpoint)