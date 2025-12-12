"""
Mighty Networks SDK Exceptions

Custom exception classes for the Mighty Networks SDK.
"""

class MightyNetworksException(Exception):
    """Base exception for all Mighty Networks SDK errors."""
    pass


class AuthenticationError(MightyNetworksException):
    """Raised when authentication fails."""
    pass


class ResourceNotFoundError(MightyNetworksException):
    """Raised when a requested resource is not found (404)."""
    pass


class ValidationError(MightyNetworksException):
    """Raised when request validation fails (422)."""
    pass


class RateLimitError(MightyNetworksException):
    """Raised when API rate limit is exceeded."""
    pass


class APIError(MightyNetworksException):
    """Raised for general API errors."""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response
