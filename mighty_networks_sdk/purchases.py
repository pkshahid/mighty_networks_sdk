"""
Purchases Resource

Handles all purchase-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class PurchasesResource(BaseResource):
    """
    Manage one-time purchases and transactions.

    Purchases track one-time payments for courses, products, etc.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all purchases in a network.

        Args:
            network_id: The network ID

        Returns:
            List of purchases

        Example:
            >>> client.purchases.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/purchases"
        params = {}
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
        endpoint = f"/admin/v1/networks/{network_id}/purchases/{purchase_id}/"
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
        endpoint = f"/admin/v1/networks/{network_id}/purchases/{purchase_id}/refund"
        data = {}
        if amount is not None:
            data["amount"] = amount
        if reason:
            data["reason"] = reason
        return self._post(endpoint, json=data)
