from tests.base import BaseTestCase # noqa
from fixtures.users.signin_user_fixtures import (
    signin_user_mutation,
    signin_user_mutation_response
) # noqa


class TestSigninUser(BaseTestCase):
    def test_signin_user_(self):
        """Test sign in a user."""
        user = self.client.execute(signin_user_mutation)
        self.assertEquals(user, signin_user_mutation_response)
