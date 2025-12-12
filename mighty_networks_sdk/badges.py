"""
Badges Resource

Handles all badge-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class BadgesResource(BaseResource):
    """
    Manage achievement badges.

    Badges recognize member achievements and contributions.
    """

    def list(
        self,
        network_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List all badges in a network.

        Args:
            network_id: The network ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of badges

        Example:
            >>> client.badges.list(network_id=12345)
        """
        endpoint = f"admin/v1/networks/{network_id}/badges"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def get(self, network_id: int, badge_id: int) -> Dict[str, Any]:
        """
        Get a specific badge by ID.

        Args:
            network_id: The network ID
            badge_id: The badge ID

        Returns:
            Badge details

        Example:
            >>> client.badges.get(network_id=12345, badge_id=333)
        """
        endpoint = f"admin/v1/networks/{network_id}/badges/{badge_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        description: str,
        image_url: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new badge.

        Args:
            network_id: The network ID
            name: Badge name
            description: Badge description
            image_url: Badge image URL
            **kwargs: Additional badge properties

        Returns:
            Created badge details

        Example:
            >>> client.badges.create(
            ...     network_id=12345,
            ...     name="Top Contributor",
            ...     description="Awarded for outstanding contributions",
            ...     image_url="https://example.com/badge.png"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/badges"
        data = {
            "name": name,
            "description": description,
            "image_url": image_url,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        badge_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a badge.

        Args:
            network_id: The network ID
            badge_id: The badge ID
            **kwargs: Badge properties to update

        Returns:
            Updated badge details

        Example:
            >>> client.badges.update(
            ...     network_id=12345,
            ...     badge_id=333,
            ...     description="Updated description"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/badges/{badge_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(self, network_id: int, badge_id: int) -> Dict[str, Any]:
        """
        Delete a badge.

        Args:
            network_id: The network ID
            badge_id: The badge ID

        Returns:
            Empty response on success

        Example:
            >>> client.badges.delete(network_id=12345, badge_id=333)
        """
        endpoint = f"admin/v1/networks/{network_id}/badges/{badge_id}/"
        return self._delete(endpoint)

    def award(
        self,
        network_id: int,
        badge_id: int,
        user_id: int
    ) -> Dict[str, Any]:
        """
        Award a badge to a member.

        Args:
            network_id: The network ID
            badge_id: The badge ID
            user_id: The user ID to award the badge to

        Returns:
            Award details

        Example:
            >>> client.badges.award(
            ...     network_id=12345,
            ...     badge_id=333,
            ...     user_id=99999
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/badges/{badge_id}/award"
        data = {"user_id": user_id}
        return self._post(endpoint, json=data)
