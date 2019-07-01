import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.add_category_fixtures import (
    add_category_mutation,
    add_category_mutation_response,
    add_category_with_no_name_mutation,
    add_duplicate_category_mutation
) # noqa


class TestAddCategory(BaseTestCase):
    def test_add_category(self):
        """Test adding category."""
        category = self.client.execute(add_category_mutation, context_value=self.valid_user_token)
        self.assertEquals(category, add_category_mutation_response)

    def test_add_category_without_name(self):
        """Test adding category without name."""
        category = self.client.execute(add_category_with_no_name_mutation, context_value=self.valid_user_token)
        self.assertIn("Category name cannot be empty", str(category))

    def test_add_existing_category(self):
        """Test adding category that already exists."""
        category = self.client.execute(add_duplicate_category_mutation, context_value=self.valid_user_token) # noqa
        self.assertIn("Category already exists", str(category))
