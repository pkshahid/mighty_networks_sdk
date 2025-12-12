"""
Tests for MembersResource
"""
import pytest
from unittest.mock import Mock, patch
from mighty_networks_sdk import MightyNetworksClient


@pytest.fixture
def client():
    """Create a test client."""
    return MightyNetworksClient(api_token="test_token")


class TestMembersResource:
    """Test cases for MembersResource."""

    def test_list_members(self, client):
        """Test listing members."""
        mock_response = {
            'items': [
                {
                    'id': 99999,
                    'email': 'user@example.com',
                    'first_name': 'John',
                    'last_name': 'Doe'
                }
            ],
            'links': {'self': 'https://api.mn.co/admin/v1/networks/12345/members'}
        }

        with patch.object(client.members, '_get', return_value=mock_response):
            result = client.members.list(network_id=12345)

            assert len(result['items']) == 1
            assert result['items'][0]['email'] == 'user@example.com'

    def test_get_member(self, client):
        """Test getting a specific member."""
        mock_member = {
            'id': 99999,
            'email': 'user@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        with patch.object(client.members, '_get', return_value=mock_member):
            result = client.members.get(
                network_id=12345,
                user_id=99999,
                space_id=67890
            )

            assert result['id'] == 99999
            assert result['first_name'] == 'John'

    def test_add_member_to_space(self, client):
        """Test adding a member to a space."""
        mock_member = {
            'id': 99999,
            'email': 'newuser@example.com',
            'first_name': 'Jane',
            'role': 'member'
        }

        with patch.object(client.members, '_post', return_value=mock_member):
            result = client.members.add_to_space(
                network_id=12345,
                space_id=67890,
                email='newuser@example.com',
                first_name='Jane',
                role='member'
            )

            assert result['email'] == 'newuser@example.com'
            assert result['role'] == 'member'

    def test_update_member_role(self, client):
        """Test updating a member's role."""
        mock_member = {
            'id': 99999,
            'email': 'user@example.com',
            'role': 'moderator'
        }

        with patch.object(client.members, '_patch', return_value=mock_member):
            result = client.members.update(
                network_id=12345,
                user_id=99999,
                space_id=67890,
                role='moderator'
            )

            assert result['role'] == 'moderator'

    def test_ban_member(self, client):
        """Test banning a member."""
        with patch.object(client.members, '_post', return_value={}):
            result = client.members.ban(
                network_id=12345,
                user_id=99999,
                space_id=67890,
                ban_reason="Violation of guidelines"
            )

            assert result == {}

    def test_remove_member(self, client):
        """Test removing a member from a space."""
        with patch.object(client.members, '_delete', return_value={}):
            result = client.members.remove(
                network_id=12345,
                user_id=99999,
                space_id=67890
            )

            assert result == {}
