import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.query_categories_fixtures import (
    query_all_categories_query,
    query_all_categories_query_response,
    query_categories_with_favorites_query,
    query_categories_with_favorites_query_response
) # noqa


class TestQueryCategories(BaseTestCase):
    def test_query_all_categories(self):
        """Test query all categories."""
        all_categories = self.client.execute(query_all_categories_query, context_value=self.valid_user_token)
        self.assertEquals(all_categories, query_all_categories_query_response)

    def test_query_categories_with_favorites(self):
        """Test query categories that have favorites."""
        categories_favorites = self.client.execute(query_categories_with_favorites_query, context_value=self.valid_user_token) # noqa
        self.assertEquals(categories_favorites, query_categories_with_favorites_query_response)
