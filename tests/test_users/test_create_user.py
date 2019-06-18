import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase
from fixtures.users.create_user_fixtures import (
    create_user_mutation,
    create_user_mutation_response
)

class TestCreateUser(BaseTestCase):
    def test_create_user_(self):
        user = self.client.execute(create_user_mutation)
        self.assertEquals(user, create_user_mutation_response)
