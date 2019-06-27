import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.categories.delete_category_fixtures import (
    delete_category_mutation,
    delete_category_mutation_response,
    delete_category_with_non_existent_id_mutation,
    delete_category_with_favorite_mutation
) # noqa


class TestDeleteCategory(BaseTestCase):
    def test_delete_category(self):
        category = self.client.execute(delete_category_mutation, context_value={'Access-Token': self.token})
        self.assertEquals(category, delete_category_mutation_response)

    def test_delete_category_with_non_existent_id(self):
        category = self.client.execute(
            delete_category_with_non_existent_id_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn("Category does not exist", str(category))

    def test_delete_category_with_favorite(self):
        category = self.client.execute(
            delete_category_with_favorite_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn("Cannot delete category because it has favorite things", str(category))