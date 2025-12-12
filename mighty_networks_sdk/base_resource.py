import httpx
from typing import Dict, Any, Optional
from .exceptions import (
    APIError,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
)


class BaseResource:
    def __init__(self, client):
        self.client = client

        # HTTP/2 client solves Cloudflare fingerprint blocking
        self._session = httpx.Client(http2=True, timeout=getattr(client, "timeout", 30))

        # Chrome-like headers to bypass Cloudflare bot detection
        self._default_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            # Admin API uses Token auth (not Bearer)
            "Authorization": f"Bearer {self.client.api_token}",
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        # Clean base URL
        base_url = self.client.base_url.rstrip("/")
        url = f"{base_url}{endpoint}"

        headers = dict(self._default_headers)

        if json is not None and files is None:
            headers["Content-Type"] = "application/json"

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                data=data,
                files=files,
            )

            # -------------------------
            # Handle non-success codes
            # -------------------------
            if response.status_code == 401:
                return {"status": False, "data": [], "message": "Unauthorized (401)"}

            if response.status_code == 403:
                return {"status": False, "data": [], "message": "Forbidden (403): Access denied"}

            if response.status_code == 404:
                return {"status": False, "data": [], "message": f"Not found: {url}"}

            if response.status_code == 429:
                return {"status": False, "data": [], "message": "Rate limit exceeded"}

            if response.status_code >= 400:
                try:
                    err = response.json()
                except Exception:
                    err = response.text
                return {"status": False, "data": [], "message": f"Error {response.status_code}: {err}"}

            # -------------------------
            # Parse successful response
            # -------------------------
            try:
                body = response.json()
            except Exception:
                body = {}

            # Normalize items
            items = []

            if isinstance(body, dict):
                if "items" in body:
                    items = body["items"]
                else:
                    # fallback: treat whole body as list or single item
                    if isinstance(body, list):
                        items = body
                    else:
                        items = body

            return {"status": True, "data": items, "message": "success"}

        except httpx.RequestError as e:
            return {
                "status": False,
                "data": [],
                "message": f"Network error: {str(e)}"
            }


    # Public request helpers
    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None):
        return self._request("GET", endpoint, params=params)

    def _post(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ):
        return self._request("POST", endpoint, json=json, data=data, files=files)

    def _put(self, endpoint: str, json: Optional[Dict[str, Any]] = None):
        return self._request("PUT", endpoint, json=json)

    def _patch(self, endpoint: str, json: Optional[Dict[str, Any]] = None):
        return self._request("PATCH", endpoint, json=json)

    def _delete(self, endpoint: str):
        return self._request("DELETE", endpoint)
