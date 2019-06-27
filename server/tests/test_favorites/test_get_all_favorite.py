import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.get_all_favorite_fixtures import (
    get_all_favorite_query,
    get_all_favorite_response
) # noqa


class TestGetAllFavorite(BaseTestCase):
    def test_get_all_favorite(self):
        favorites = self.client.execute(get_all_favorite_query, context_value={'Access-Token': self.token})
        self.assertEquals(favorites, get_all_favorite_response)
