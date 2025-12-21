"""
Network Resource
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class NetworkResource(BaseResource):
    """
    Return information about the network
    """

    def show(self, network_id: int) -> Dict[str, Any]:
        """
        Get the network details.

        Args:
            network_id: The network ID

        Returns:
            details

        Example:
            >>> client.network.show(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}"
        return self._get(endpoint)