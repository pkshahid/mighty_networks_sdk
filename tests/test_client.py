"""
Tests for MightyNetworksClient
"""
import pytest
from mighty_networks_sdk import MightyNetworksClient
from mighty_networks_sdk.exceptions import MightyNetworksException

def test_client_initialization():
    """Test client initialization."""
    client = MightyNetworksClient(api_token="test_token")
    assert client.api_token == "test_token"
    assert client.base_url == "https://api.mn.co"
    assert client.timeout == 30

def test_client_missing_token():
    """Test client initialization without token."""
    with pytest.raises(ValueError):
        MightyNetworksClient(api_token="")

def test_client_custom_config():
    """Test client with custom configuration."""
    client = MightyNetworksClient(
        api_token="test_token",
        base_url="https://custom.api.com",
        timeout=60
    )
    assert client.base_url == "https://custom.api.com"
    assert client.timeout == 60

def test_client_repr():
    """Test client string representation."""
    client = MightyNetworksClient(api_token="test_token")
    assert "MightyNetworksClient" in repr(client)
