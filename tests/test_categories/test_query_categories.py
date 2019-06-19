import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.query_categories_fixtures import (
    query_all_categories_query,
    query_all_categories_query_response
) # noqa


class TestQueryCategories(BaseTestCase):
    def test_query_all_categories(self):
        all_categories = self.client.execute(query_all_categories_query)
        self.assertEquals(all_categories, query_all_categories_query_response)
