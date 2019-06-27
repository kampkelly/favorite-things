import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.get_single_favorite_fixtures import (
    get_single_favorite_query,
    get_single_favorite_query_response,
    get_single_favorite_with_non_existing_id_query
) # noqa


class TestGetSingleFavorite(BaseTestCase):
    def test_get_single_favorite(self):
        favorite = self.client.execute(
            get_single_favorite_query,
            context_value={'Access-Token': self.token})
        self.assertEquals(favorite, get_single_favorite_query_response)

    def test_get_single_favorite_with_non_existing_id(self):
        favorite = self.client.execute(
            get_single_favorite_with_non_existing_id_query,
            context_value={'Access-Token': self.token})
        self.assertIn('Favorite thing does not exist', str(favorite))
