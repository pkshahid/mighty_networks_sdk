"""
Polls Resource

Handles all poll-related API operations.
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class PollsResource(BaseResource):
    """
    Manage polls within posts.

    Polls allow members to vote on questions.
    """

    def list(
        self,
        network_id: int,
        space_id: int
    ) -> Dict[str, Any]:
        """
        List polls in a space.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            List of polls

        Example:
            >>> client.polls.list(network_id=12345, space_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/polls"
        params = {}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        space_id: int,
        poll_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific poll by ID.

        Args:
            network_id: The network ID
            space_id: The space ID
            poll_id: The poll ID

        Returns:
            Poll details including results

        Example:
            >>> client.polls.get(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     poll_id=44444
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/polls/{poll_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        space_id: int,
        question: str,
        options: List[str],
        allow_multiple: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new poll.

        Args:
            network_id: The network ID
            space_id: The space ID
            question: Poll question
            options: List of poll options
            allow_multiple: Allow multiple selections (default: False)
            **kwargs: Additional poll properties

        Returns:
            Created poll details

        Example:
            >>> client.polls.create(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     question="What's your favorite feature?",
            ...     options=["Feature A", "Feature B", "Feature C"],
            ...     allow_multiple=False
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/polls"
        data = {
            "question": question,
            "options": options,
            "allow_multiple": allow_multiple,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        space_id: int,
        poll_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a poll.

        Args:
            network_id: The network ID
            space_id: The space ID
            poll_id: The poll ID
            **kwargs: Poll properties to update

        Returns:
            Updated poll details

        Example:
            >>> client.polls.update(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     poll_id=44444,
            ...     question="Updated question?"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/polls/{poll_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(
        self,
        network_id: int,
        space_id: int,
        poll_id: int
    ) -> Dict[str, Any]:
        """
        Delete a poll.

        Args:
            network_id: The network ID
            space_id: The space ID
            poll_id: The poll ID

        Returns:
            Empty response on success

        Example:
            >>> client.polls.delete(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     poll_id=44444
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/polls/{poll_id}/"
        return self._delete(endpoint)
