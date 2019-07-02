import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.get_all_favorite_fixtures import (
    get_all_favorite_query,
) # noqa


class TestUserToken(BaseTestCase):
    def test_empty_token_logs(self):
        """Test for empty token."""
        favorites = self.client.execute(get_all_favorite_query, context_value={'no-token': self.token})
        self.assertIn("Access Token is empty", str(favorites))

    def test_invalid_token_logs(self):
        """Test for invalid token."""
        favorites = self.client.execute(get_all_favorite_query, context_value={'Access-Token': '1234'})
        self.assertIn("Access Token is invalid", str(favorites))

    def test_expired_token_logs(self):
        """Test for expired token."""
        favorites = self.client.execute(get_all_favorite_query, context_value={'Access-Token': self.expired_token})
        self.assertIn("Access Token has expired", str(favorites))
