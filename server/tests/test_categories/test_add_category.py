import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.add_category_fixtures import (
    add_category_mutation,
    add_category_mutation_response
) # noqa


class TestAddCategory(BaseTestCase):
    def test_add_category(self):
        category = self.client.execute(add_category_mutation)
        self.assertEquals(category, add_category_mutation_response)
