"""
Base Resource Class

Provides common functionality for all resource classes.
"""

import requests
from typing import Dict, Any, Optional
from .exceptions import (
    APIError,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError
)


class BaseResource:
    """Base class for all API resources."""

    def __init__(self, client):
        """
        Initialize the resource with a client instance.

        Args:
            client: The MightyNetworksClient instance
        """
        self.client = client

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            data: Form data
            json: JSON body data

        Returns:
            Response data as dictionary

        Raises:
            AuthenticationError: If authentication fails
            ResourceNotFoundError: If resource not found
            ValidationError: If request validation fails
            RateLimitError: If rate limit exceeded
            APIError: For other API errors
        """
        url = f"{self.client.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.client.api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                data=data,
                timeout=self.client.timeout
            )

            # Handle different status codes
            if response.status_code == 401:
                raise AuthenticationError("Invalid or expired API token")
            elif response.status_code == 404:
                raise ResourceNotFoundError(f"Resource not found: {endpoint}")
            elif response.status_code == 422:
                error_data = response.json() if response.content else {}
                raise ValidationError(f"Validation error: {error_data}")
            elif response.status_code == 429:
                raise RateLimitError("API rate limit exceeded")
            elif response.status_code >= 400:
                error_data = response.json() if response.content else {}
                raise APIError(
                    f"API error: {error_data}",
                    status_code=response.status_code,
                    response=error_data
                )

            # Return response data
            if response.content:
                return response.json()
            return {}

        except requests.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request."""
        return self._request("GET", endpoint, params=params)

    def _post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request."""
        return self._request("POST", endpoint, json=json)

    def _put(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PUT request."""
        return self._request("PUT", endpoint, json=json)

    def _patch(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PATCH request."""
        return self._request("PATCH", endpoint, json=json)

    def _delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self._request("DELETE", endpoint)
