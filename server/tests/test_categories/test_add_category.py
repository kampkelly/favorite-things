import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.add_category_fixtures import (
    add_category_mutation,
    add_category_mutation_response,
    add_category_with_no_name_mutation
) # noqa


class TestAddCategory(BaseTestCase):
    def test_add_category(self):
        category = self.client.execute(add_category_mutation, context_value={'Access-Token': self.token})
        self.assertEquals(category, add_category_mutation_response)

    def test_add_category_without_name(self):
        category = self.client.execute(add_category_with_no_name_mutation, context_value={'Access-Token': self.token})
        self.assertIn("Category name cannot be empty", str(category))

    def test_add_existing_category(self):
        self.maxDiff = None
        category = self.client.execute(add_category_mutation, context_value={'Access-Token': self.token}) # noqa
        # self.assertIn("Category already exists", str(category))
