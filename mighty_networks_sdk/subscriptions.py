"""
Subscriptions Resource

Handles all subscription-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class SubscriptionsResource(BaseResource):
    """
    Manage member subscriptions to plans.

    Subscriptions track member payments and access to plans.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all subscriptions in a network.

        Args:
            network_id: The network ID

        Returns:
            Lsist of subscriptions

        Example:
            >>> client.subscriptions.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/subscriptions"
        params = {}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        subscription_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific subscription by ID.

        Args:
            network_id: The network ID
            subscription_id: The subscription ID

        Returns:
            Subscription details

        Example:
            >>> client.subscriptions.get(
            ...     network_id=12345,
            ...     subscription_id=888
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/subscriptions/{subscription_id}/"
        return self._get(endpoint)

    def cancel(
        self,
        network_id: int,
        subscription_id: int,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cancel a subscription.

        Args:
            network_id: The network ID
            subscription_id: The subscription ID
            reason: Cancellation reason (optional)

        Returns:
            Updated subscription details

        Example:
            >>> client.subscriptions.cancel(
            ...     network_id=12345,
            ...     subscription_id=888,
            ...     reason="User request"
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/subscriptions/{subscription_id}/cancel"
        data = {}
        if reason:
            data["reason"] = reason
        return self._post(endpoint, json=data)
