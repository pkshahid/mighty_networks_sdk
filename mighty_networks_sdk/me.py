"""
Me Resource
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class MeResource(BaseResource):
    """
    Return information about the authenticated access token
    """

    def show(self, network_id: int) -> Dict[str, Any]:
        """
        Get a details.

        Args:
            network_id: The network ID

        Returns:
            details

        Example:
            >>> client.me.show(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/me"
        return self._get(endpoint)