"""
Assets Resource

Handles all asset-related API operations.
"""

from typing import Dict, Any
from .base_resource import BaseResource


class AssetsResource(BaseResource):
    """
    Manage media assets like images and files.

    Assets are files uploaded to your network.
    """

    def upload(
        self,
        network_id: int,
        file_path: str,
        asset_type: str = "image"
    ) -> Dict[str, Any]:
        """
        Upload an asset file.

        Args:
            network_id: The network ID
            file_path: Path to the file to upload
            asset_type: Type of asset (image, file, etc.)

        Returns:
            Uploaded asset details including URL

        Example:
            >>> client.assets.upload(
            ...     network_id=12345,
            ...     file_path="/path/to/image.jpg",
            ...     asset_type="image"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/assets"
        # Note: Actual file upload implementation would use multipart/form-data
        # This is a simplified version
        data = {"asset_type": asset_type, "file_path": file_path}
        return self._post(endpoint, json=data)
