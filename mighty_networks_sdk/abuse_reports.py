"""
Abuse Reports Resource

Handles all abuse report-related API operations.
"""

from typing import Dict, Any
from .base_resource import BaseResource


class AbuseReportsResource(BaseResource):
    """
    Manage abuse and content reports.

    Abuse reports flag inappropriate content or behavior.
    """

    def list(
        self,
        network_id: int,
        page: int = 1,
        per_page: int = 25,
        status: str = "pending"
    ) -> Dict[str, Any]:
        """
        List abuse reports in a network.

        Args:
            network_id: The network ID
            page: Page number for pagination (default: 1)
            per_page: Items per page, max 100 (default: 25)
            status: Filter by status (pending, resolved, dismissed)

        Returns:
            Paginated list of abuse reports

        Example:
            >>> client.abuse_reports.list(
            ...     network_id=12345,
            ...     status="pending"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/abuse_reports"
        params = {"page": page, "per_page": per_page, "status": status}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        report_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific abuse report by ID.

        Args:
            network_id: The network ID
            report_id: The report ID

        Returns:
            Abuse report details

        Example:
            >>> client.abuse_reports.get(
            ...     network_id=12345,
            ...     report_id=555
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/abuse_reports/{report_id}/"
        return self._get(endpoint)

    def resolve(
        self,
        network_id: int,
        report_id: int,
        action: str,
        notes: str = ""
    ) -> Dict[str, Any]:
        """
        Resolve an abuse report.

        Args:
            network_id: The network ID
            report_id: The report ID
            action: Action taken (removed, warning, dismissed, etc.)
            notes: Resolution notes (optional)

        Returns:
            Updated report details

        Example:
            >>> client.abuse_reports.resolve(
            ...     network_id=12345,
            ...     report_id=555,
            ...     action="removed",
            ...     notes="Content violated community guidelines"
            ... )
        """
        endpoint = f"admin/v1/networks/{network_id}/abuse_reports/{report_id}/resolve"
        data = {"action": action, "notes": notes}
        return self._post(endpoint, json=data)
