import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.users.get_user_logs_fixtures import (
    user_logs_query
) # noqa
from fixtures.favorites.add_favorite_fixtures import (
    add_favorite_mutation
) # noqa


class TestGetUserLogs(BaseTestCase):
    def test_get_user_logs(self):
        """Test query user logs."""
        self.client.execute(
            add_favorite_mutation,
            context_value=self.valid_user_token)
        user_logs = self.client.execute(user_logs_query, context_value=self.valid_user_token) # noqa
        self.assertIn("You added a new", str(user_logs))
