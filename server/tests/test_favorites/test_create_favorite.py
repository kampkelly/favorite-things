import sys
import os

sys.path.append(os.getcwd())

from tests.base import BaseTestCase # noqa
from fixtures.favorites.add_favorite_fixtures import (
    add_favorite_mutation,
    add_favorite_mutation_response,
    add_favorite_with_empty_title_mutation,
    add_favorite_with_no_title_mutation,
    add_favorite_with_no_category_id_mutation,
    add_favorite_with_no_ranking_mutation,
    add_favorite_with_description_less_than_10_characters
) # noqa


class TestCreateFavorite(BaseTestCase):
    def test_create_favorite(self):
        favorite = self.client.execute(
            add_favorite_mutation,
            context_value={'Access-Token': self.token})
        self.assertEquals(favorite, add_favorite_mutation_response)

    def test_add_favorite_with_empty_title(self):
        favorite = self.client.execute(
            add_favorite_with_empty_title_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn("Title cannot be empty", str(favorite))

    def test_add_favorite_with_no_title(self):
        favorite = self.client.execute(
            add_favorite_with_no_title_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"title\" of type \"String!\" is required but not provided', str(favorite))

    def test_add_favorite_with_no_category_id(self):
        favorite = self.client.execute(
            add_favorite_with_no_category_id_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"categoryId\" of type \"Int!\" is required but not provided', str(favorite))

    def test_add_favorite_with_no_ranking(self):
        favorite = self.client.execute(
            add_favorite_with_no_ranking_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"ranking\" of type \"Int!\" is required but not provided', str(favorite))

    def test_add_favorite_with_description_less_than_10_characters(self):
        favorite = self.client.execute(
            add_favorite_with_description_less_than_10_characters,
            context_value={'Access-Token': self.token})
        self.assertIn('Description must be at least 10 characters', str(favorite))
