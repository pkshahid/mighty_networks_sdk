import os
from .base_resource import BaseResource
from typing import Dict, Any, Optional

"""
Assets Resource

Handles all asset-related API operations.
"""


class AssetsResource(BaseResource):
    
    """
    Manage media assets like images and files.

    Assets are files uploaded to your network.
    """
    
    def upload(
        self,
        network_id: int,
        file_path: Optional[str] = None,
        asset_style: str = "post",
        source_url: Optional[str] = None,
        input_type: int = 0,
        original_aspect_ratio: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
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
        
        endpoint = f"/admin/v1/networks/{network_id}/assets"
        if not file_path and not source_url:
            raise ValueError("Provide file_path or source_url")

        data = {"asset_style": asset_style, "input_type": input_type}
        if source_url:
            data["source_url"] = source_url
        if original_aspect_ratio:
            data["original_aspect_ratio"] = original_aspect_ratio
        if metadata:
            import json as _json
            data["metadata"] = _json.dumps(metadata)

        files = None
        if file_path:
            if not os.path.exists(file_path):
                raise ValueError("file_path does not exist")
            files = {"asset_file": open(file_path, "rb")}

        try:
            return self._post(endpoint, data=data, files=files)
        finally:
            if files:
                files["asset_file"].close()

