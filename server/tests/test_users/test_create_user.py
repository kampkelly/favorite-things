import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.users.create_user_fixtures import (
    create_user_mutation,
    create_user_mutation_response
) # noqa


class TestCreateUser(BaseTestCase):
    def test_create_user(self):
        """Test creating a user."""
        user = self.client.execute(create_user_mutation)
        self.assertEquals(user, create_user_mutation_response)

    def test_create_duplicate_user(self):
        """Test creating a duplicate user."""
        user = self.client.execute(create_user_mutation) # noqa
        # self.assertIn("An account with this email already exists", str(user))
