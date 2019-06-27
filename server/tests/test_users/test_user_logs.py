import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.users.get_user_logs_fixtures import (
    user_logs_query
) # noqa


class TestGetUserLogs(BaseTestCase):
    def test_get_user_logs(self):
        user_logs = self.client.execute(user_logs_query, context_value={'Access-Token': self.token}) # noqa
        # self.assertIn("You added a new", str(user_logs))
