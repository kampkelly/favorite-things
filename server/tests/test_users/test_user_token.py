import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.get_all_favorite_fixtures import (
    get_all_favorite_query,
) # noqa


class TestUserToken(BaseTestCase):
    def test_get_user_logs(self):
        favorites = self.client.execute(get_all_favorite_query, context_value={'no-token': self.token})
        self.assertIn("Access Token is empty", str(favorites))
