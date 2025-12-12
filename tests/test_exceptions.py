"""
Tests for exception handling
"""
import pytest
from mighty_networks_sdk.exceptions import (
    MightyNetworksException,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
    APIError
)


class TestExceptions:
    """Test exception classes."""

    def test_base_exception(self):
        """Test base exception."""
        error = MightyNetworksException("Test error")
        assert str(error) == "Test error"
        assert isinstance(error, Exception)

    def test_authentication_error(self):
        """Test authentication error."""
        error = AuthenticationError("Invalid token")
        assert str(error) == "Invalid token"
        assert isinstance(error, MightyNetworksException)

    def test_resource_not_found_error(self):
        """Test resource not found error."""
        error = ResourceNotFoundError("Space not found")
        assert str(error) == "Space not found"
        assert isinstance(error, MightyNetworksException)

    def test_validation_error(self):
        """Test validation error."""
        error = ValidationError("Invalid input")
        assert str(error) == "Invalid input"
        assert isinstance(error, MightyNetworksException)

    def test_rate_limit_error(self):
        """Test rate limit error."""
        error = RateLimitError("Too many requests")
        assert str(error) == "Too many requests"
        assert isinstance(error, MightyNetworksException)

    def test_api_error(self):
        """Test API error with status code."""
        error = APIError("Server error", status_code=500, response={"error": "Internal"})
        assert str(error) == "Server error"
        assert error.status_code == 500
        assert error.response == {"error": "Internal"}
        assert isinstance(error, MightyNetworksException)
