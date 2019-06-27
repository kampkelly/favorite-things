import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.update_favorite_fixtures import (
    update_favorite_mutation,
    update_favorite_mutation_response,
    update_favorite_with_no_id_mutation,
    update_favorite_with_no_ranking_mutation,
    update_favorite_with_empty_title_mutation,
    update_favorite_with_description_less_than_10_characters
) # noqa


class TestUpdateFavorite(BaseTestCase):
    def test_update_favorite(self):
        favorite = self.client.execute(
            update_favorite_mutation,
            context_value={'Access-Token': self.token})
        self.assertEquals(favorite, update_favorite_mutation_response)

    def test_update_favorite_with_empty_title(self):
        favorite = self.client.execute(
            update_favorite_with_empty_title_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn("Title cannot be empty", str(favorite))

    def test_update_favorite_with_no_id(self):
        favorite = self.client.execute(
            update_favorite_with_no_id_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"id\" of type \"Int!\" is required but not provide', str(favorite))

    def test_update_favorite_with_no_ranking(self):
        favorite = self.client.execute(
            update_favorite_with_no_ranking_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"ranking\" of type \"Int!\" is required but not provided', str(favorite))

    def test_update_favorite_with_description_less_than_10_characters(self):
        favorite = self.client.execute(
            update_favorite_with_description_less_than_10_characters,
            context_value={'Access-Token': self.token})
        self.assertIn('Description must be at least 10 characters', str(favorite))
