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
        """Test query a single favorite thing."""
        favorite = self.client.execute(
            get_single_favorite_query,
            context_value=self.valid_user_token)
        self.assertEquals(favorite, get_single_favorite_query_response)

    def test_get_single_favorite_with_non_existing_id(self):
        """Test query a single favorite thing with id that does not exist."""
        favorite = self.client.execute(
            get_single_favorite_with_non_existing_id_query,
            context_value=self.valid_user_token)
        self.assertIn('Favorite thing does not exist', str(favorite))
