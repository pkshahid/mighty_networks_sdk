"""
Tests for SpacesResource
"""
import pytest
from unittest.mock import Mock, patch
from mighty_networks_sdk import MightyNetworksClient
from mighty_networks_sdk.exceptions import ResourceNotFoundError


@pytest.fixture
def client():
    """Create a test client."""
    return MightyNetworksClient(api_token="test_token")


@pytest.fixture
def mock_response():
    """Create a mock response."""
    return {
        'items': [
            {
                'id': 67890,
                'name': 'Test Space',
                'description': 'A test space',
                'is_public': True
            }
        ],
        'links': {'self': 'https://api.mn.co/admin/v1/networks/12345/spaces'}
    }


class TestSpacesResource:
    """Test cases for SpacesResource."""

    def test_list_spaces(self, client, mock_response):
        """Test listing spaces."""
        with patch.object(client.spaces, '_get', return_value=mock_response):
            result = client.spaces.list(network_id=12345)

            assert 'items' in result
            assert len(result['items']) == 1
            assert result['items'][0]['name'] == 'Test Space'

    def test_get_space(self, client):
        """Test getting a specific space."""
        mock_space = {
            'id': 67890,
            'name': 'Test Space',
            'description': 'A test space'
        }

        with patch.object(client.spaces, '_get', return_value=mock_space):
            result = client.spaces.get(network_id=12345, space_id=67890)

            assert result['id'] == 67890
            assert result['name'] == 'Test Space'

    def test_create_space(self, client):
        """Test creating a space."""
        mock_space = {
            'id': 67890,
            'name': 'New Space',
            'description': 'A new space',
            'is_public': True
        }

        with patch.object(client.spaces, '_post', return_value=mock_space):
            result = client.spaces.create(
                network_id=12345,
                name='New Space',
                description='A new space'
            )

            assert result['name'] == 'New Space'
            assert result['is_public'] is True

    def test_update_space(self, client):
        """Test updating a space."""
        mock_space = {
            'id': 67890,
            'name': 'Updated Space',
            'description': 'Updated description'
        }

        with patch.object(client.spaces, '_patch', return_value=mock_space):
            result = client.spaces.update(
                network_id=12345,
                space_id=67890,
                name='Updated Space'
            )

            assert result['name'] == 'Updated Space'

    def test_delete_space(self, client):
        """Test deleting a space."""
        with patch.object(client.spaces, '_delete', return_value={}):
            result = client.spaces.delete(network_id=12345, space_id=67890)

            assert result == {}

    def test_space_not_found(self, client):
        """Test handling of space not found error."""
        with patch.object(client.spaces, '_get', side_effect=ResourceNotFoundError("Not found")):
            with pytest.raises(ResourceNotFoundError):
                client.spaces.get(network_id=12345, space_id=99999)
