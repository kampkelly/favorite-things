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
        self.assertIn("Authorization code is empty", str(favorites))

    def test_invalid_token_logs(self):
        """Test for invalid token."""
        favorites = self.client.execute(get_all_favorite_query, context_value={'user-key': '1234'})
        self.assertIn("Invalid token supplied", str(favorites))

    def test_expired_token_logs(self):
        """Test for expired token."""
        favorites = self.client.execute(get_all_favorite_query, context_value=self.expired_user_token)
        self.assertIn("Authorization code has expired", str(favorites))
