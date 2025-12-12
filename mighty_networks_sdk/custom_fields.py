"""
Custom Fields Resource

Handles all custom field-related API operations.
"""

from typing import Dict, Any, Optional, List
from .base_resource import BaseResource


class CustomFieldsResource(BaseResource):
    """
    Manage custom fields for member profiles.

    Custom fields allow you to collect additional information from members.
    """

    def list(
        self,
        network_id: int
    ) -> Dict[str, Any]:
        """
        List all custom fields in a network.

        Args:
            network_id: The network ID

        Returns:
            List of custom fields

        Example:
            >>> client.custom_fields.list(network_id=12345)
        """
        endpoint = f"/admin/v1/networks/{network_id}/custom_fields"
        params = {}
        return self._get(endpoint, params=params)

    def get(self, network_id: int, field_id: int) -> Dict[str, Any]:
        """
        Get a specific custom field by ID.

        Args:
            network_id: The network ID
            field_id: The custom field ID

        Returns:
            Custom field details

        Example:
            >>> client.custom_fields.get(network_id=12345, field_id=456)
        """
        endpoint = f"/admin/v1/networks/{network_id}/custom_fields/{field_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        name: str,
        field_type: str,
        required: bool = False,
        options: Optional[List[str]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new custom field.

        Args:
            network_id: The network ID
            name: Field name
            field_type: Field type (text, textarea, select, checkbox, radio, etc.)
            required: Whether field is required (default: False)
            options: Options for select/radio fields (optional)
            **kwargs: Additional field properties

        Returns:
            Created custom field details

        Example:
            >>> client.custom_fields.create(
            ...     network_id=12345,
            ...     name="Company",
            ...     field_type="text",
            ...     required=True
            ... )

            >>> client.custom_fields.create(
            ...     network_id=12345,
            ...     name="Industry",
            ...     field_type="select",
            ...     options=["Technology", "Healthcare", "Finance", "Other"]
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/custom_fields"
        data = {
            "name": name,
            "field_type": field_type,
            "required": required,
            **kwargs
        }
        if options:
            data["options"] = options

        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        field_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a custom field.

        Args:
            network_id: The network ID
            field_id: The custom field ID
            **kwargs: Field properties to update

        Returns:
            Updated custom field details

        Example:
            >>> client.custom_fields.update(
            ...     network_id=12345,
            ...     field_id=456,
            ...     name="Updated Field Name",
            ...     required=True
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/custom_fields/{field_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(self, network_id: int, field_id: int) -> Dict[str, Any]:
        """
        Delete a custom field.

        Args:
            network_id: The network ID
            field_id: The custom field ID

        Returns:
            Empty response on success

        Example:
            >>> client.custom_fields.delete(network_id=12345, field_id=456)
        """
        endpoint = f"/admin/v1/networks/{network_id}/custom_fields/{field_id}/"
        return self._delete(endpoint)

    def get_member_values(
        self,
        network_id: int,
        user_id: int
    ) -> Dict[str, Any]:
        """
        Get custom field values for a specific member.

        Args:
            network_id: The network ID
            user_id: The user ID

        Returns:
            Dictionary of custom field values

        Example:
            >>> client.custom_fields.get_member_values(
            ...     network_id=12345,
            ...     user_id=99999
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/custom_fields"
        return self._get(endpoint)

    def update_member_values(
        self,
        network_id: int,
        user_id: int,
        field_values: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update custom field values for a specific member.

        Args:
            network_id: The network ID
            user_id: The user ID
            field_values: Dictionary of field_id: value pairs

        Returns:
            Updated custom field values

        Example:
            >>> client.custom_fields.update_member_values(
            ...     network_id=12345,
            ...     user_id=99999,
            ...     field_values={
            ...         "456": "Acme Corp",
            ...         "457": "Technology"
            ...     }
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/members/{user_id}/custom_fields"
        return self._patch(endpoint, json=field_values)
