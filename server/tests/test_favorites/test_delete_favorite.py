import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.delete_favorite_fixtures import (
    delete_favorite_mutation,
    delete_favorite_mutation_response
) # noqa


class TestDeleteFavorite(BaseTestCase):
    def test_delete_favorite(self):
        favorite = self.client.execute(delete_favorite_mutation, context_value={'Access-Token': self.token})
        self.assertEquals(favorite, delete_favorite_mutation_response)