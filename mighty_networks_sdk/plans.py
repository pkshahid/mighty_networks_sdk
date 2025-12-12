"""
Plans Resource

Handles all membership plan-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class PlansResource(BaseResource):
    """
    Manage membership plans and pricing.

    Plans define the pricing and access levels for your network.
    """

    def list(
        self,
        network_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List all plans in a network.

        Args:
            network_id: The network ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of plans

        Example:
            >>> client.plans.list(network_id=12345)
        """
        endpoint = f"admin/v1/networks/{network_id}/plans"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def get(self, network_id: int, plan_id: int) -> Dict[str, Any]:
        """
        Get a specific plan by ID.

        Args:
            network_id: The network ID
            plan_id: The plan ID

        Returns:
            Plan details

        Example:
            >>> client.plans.get(network_id=12345, plan_id=789)
        """
        endpoint = f"admin/v1/networks/{network_id}/plans/{plan_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        description: str,
        price: float,
        currency: str = "USD",
        interval: str = "month",
        trial_days: int = 0,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new membership plan.

        Args:
            network_id: The network ID
            name: Plan name
            description: Plan description
            price: Plan price
            currency: Currency code (default: USD)
            interval: Billing interval (day, week, month, year)
            trial_days: Number of trial days (default: 0)
            **kwargs: Additional plan properties

        Returns:
            Created plan details

        Example:
            >>> client.plans.create(
            ...     network_id=12345,
            ...     name="Premium Membership",
            ...     description="Full access to all features",
            ...     price=29.99,
            ...     interval="month",
            ...     trial_days=7
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/plans"
        data = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
            "interval": interval,
            "trial_days": trial_days,
            **kwargs
        }
        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        plan_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a plan.

        Args:
            network_id: The network ID
            plan_id: The plan ID
            **kwargs: Plan properties to update

        Returns:
            Updated plan details

        Example:
            >>> client.plans.update(
            ...     network_id=12345,
            ...     plan_id=789,
            ...     price=39.99,
            ...     name="Premium Plus"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/plans/{plan_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(self, network_id: int, plan_id: int) -> Dict[str, Any]:
        """
        Delete a plan.

        Args:
            network_id: The network ID
            plan_id: The plan ID

        Returns:
            Empty response on success

        Example:
            >>> client.plans.delete(network_id=12345, plan_id=789)
        """
        endpoint = f"admin/v1/networks/{network_id}/plans/{plan_id}/"
        return self._delete(endpoint)

    def get_subscribers(
        self,
        network_id: int,
        plan_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        Get subscribers for a specific plan.

        Args:
            network_id: The network ID
            plan_id: The plan ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of subscribers

        Example:
            >>> client.plans.get_subscribers(network_id=12345, plan_id=789)
        """
        endpoint = f"admin/v1/networks/{network_id}/plans/{plan_id}/subscribers"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)
