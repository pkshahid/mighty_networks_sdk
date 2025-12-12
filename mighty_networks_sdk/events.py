"""
Events Resource

Handles all event-related API operations.
"""

from typing import Dict, Any, Optional
from .base_resource import BaseResource


class EventsResource(BaseResource):
    """
    Manage events within spaces.

    Events are scheduled gatherings or activities for members.
    """

    def list(
        self,
        network_id: int,
        space_id: int
    ) -> Dict[str, Any]:
        """
        List events in a space.

        Args:
            network_id: The network ID
            space_id: The space ID

        Returns:
            List of events

        Example:
            >>> client.events.list(network_id=12345, space_id=67890)
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events"
        params = {}
        return self._get(endpoint, params=params)

    def get(
        self,
        network_id: int,
        space_id: int,
        event_id: int
    ) -> Dict[str, Any]:
        """
        Get a specific event by ID.

        Args:
            network_id: The network ID
            space_id: The space ID
            event_id: The event ID

        Returns:
            Event details

        Example:
            >>> client.events.get(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     event_id=22222
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events/{event_id}/"
        return self._get(endpoint)

    def create(
        self,
        network_id: int,
        space_id: int,
        title: str,
        description: str,
        start_time: str,
        end_time: str,
        location: Optional[str] = None,
        is_online: bool = False,
        max_attendees: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new event.

        Args:
            network_id: The network ID
            space_id: The space ID
            title: Event title
            description: Event description
            start_time: Event start time (ISO 8601 format)
            end_time: Event end time (ISO 8601 format)
            location: Event location (optional)
            is_online: Whether the event is online (default: False)
            max_attendees: Maximum number of attendees (optional)
            **kwargs: Additional event properties

        Returns:
            Created event details

        Example:
            >>> client.events.create(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     title="Community Meetup",
            ...     description="Join us for a casual meetup!",
            ...     start_time="2024-03-01T18:00:00Z",
            ...     end_time="2024-03-01T20:00:00Z",
            ...     location="San Francisco, CA",
            ...     max_attendees=50
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events"
        data = {
            "title": title,
            "description": description,
            "start_time": start_time,
            "end_time": end_time,
            "is_online": is_online,
            **kwargs
        }
        if location:
            data["location"] = location
        if max_attendees:
            data["max_attendees"] = max_attendees

        return self._post(endpoint, json=data)

    def update(
        self,
        network_id: int,
        space_id: int,
        event_id: int,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an event.

        Args:
            network_id: The network ID
            space_id: The space ID
            event_id: The event ID
            **kwargs: Event properties to update

        Returns:
            Updated event details

        Example:
            >>> client.events.update(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     event_id=22222,
            ...     title="Updated Event Title",
            ...     max_attendees=100
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events/{event_id}/"
        return self._patch(endpoint, json=kwargs)

    def delete(
        self,
        network_id: int,
        space_id: int,
        event_id: int
    ) -> Dict[str, Any]:
        """
        Delete an event.

        Args:
            network_id: The network ID
            space_id: The space ID
            event_id: The event ID

        Returns:
            Empty response on success

        Example:
            >>> client.events.delete(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     event_id=22222
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events/{event_id}/"
        return self._delete(endpoint)

    def get_attendees(
        self,
        network_id: int,
        space_id: int,
        event_id: int
    ) -> Dict[str, Any]:
        """
        Get event attendees.

        Args:
            network_id: The network ID
            space_id: The space ID
            event_id: The event ID

        Returns:
            List of attendees

        Example:
            >>> client.events.get_attendees(
            ...     network_id=12345,
            ...     space_id=67890,
            ...     event_id=22222
            ... )
        """
        endpoint = f"/admin/v1/networks/{network_id}/spaces/{space_id}/events/{event_id}/attendees"
        params = {}
        return self._get(endpoint, params=params)
