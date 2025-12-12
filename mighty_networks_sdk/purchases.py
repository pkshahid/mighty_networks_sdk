"""
Purchases Resource

Handles all purchase-related API operations.
"""

from typing import Dict, Any
from .base_resource import BaseResource


class PurchasesResource(BaseResource):
    """
    Manage one-time purchases and transactions.

    Purchases track one-time payments for courses, products, etc.
    """

    def list(
        self,
        network_id: int,
        page: int = 1,
        per_page: int = 25
    ) -> Dict[str, Any]:
        """
        List all purchases in a network.

        Args:
            network_id: The network ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)

        Returns:
            Paginated list of purchases

        Example:
            >>> client.purchases.list(network_id=12345)
        """
        endpoint = f"admin/v1/networks/{network_id}/purchases"
        params = {"page": page, "per_page": per_page}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        purchase_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific purchase by ID.

        Args:
            network_id: The network ID
            purchase_id: The purchase ID

        Returns:
            Purchase details

        Example:
            >>> client.purchases.get(
            ...     network_id=12345,
            ...     purchase_id=777
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/purchases/{purchase_id}/"
        return self._get(endpoint)

    def refund(
        self,
        network_id: int,
        purchase_id: int,
        amount: Optional[float] = None,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Refund a purchase.

        Args:
            network_id: The network ID
            purchase_id: The purchase ID
            amount: Refund amount (optional, defaults to full refund)
            reason: Refund reason (optional)

        Returns:
            Refund details

        Example:
            >>> client.purchases.refund(
            ...     network_id=12345,
            ...     purchase_id=777,
            ...     reason="Customer request"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/purchases/{purchase_id}/refund"
        data = {}
        if amount is not None:
            data["amount"] = amount
        if reason:
            data["reason"] = reason
        return self._post(endpoint, json=data)
