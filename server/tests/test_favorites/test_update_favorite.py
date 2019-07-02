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
        """Test updating a favorite thing."""
        favorite = self.client.execute(
            update_favorite_mutation,
            context_value={'Access-Token': self.token})
        self.assertEquals(favorite, update_favorite_mutation_response)

    def test_update_favorite_with_empty_title(self):
        """Test updating a favorite thing qith empty title."""
        favorite = self.client.execute(
            update_favorite_with_empty_title_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn("Title cannot be empty", str(favorite))

    def test_update_favorite_with_no_id(self):
        """Test updating a favorite thing with no id."""
        favorite = self.client.execute(
            update_favorite_with_no_id_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"id\" of type \"Int!\" is required but not provide', str(favorite))

    def test_update_favorite_with_no_ranking(self):
        """Test updating a favorite thing with no ranking."""
        favorite = self.client.execute(
            update_favorite_with_no_ranking_mutation,
            context_value={'Access-Token': self.token})
        self.assertIn('\"ranking\" of type \"Int!\" is required but not provided', str(favorite))

    def test_update_favorite_with_description_less_than_10_characters(self):
        """Test updating a favorite thing with description less than 10 characters."""
        favorite = self.client.execute(
            update_favorite_with_description_less_than_10_characters,
            context_value={'Access-Token': self.token})
        self.assertIn('Description must be at least 10 characters', str(favorite))
