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
        """Test creating a favorite thing."""
        favorite = self.client.execute(
            add_favorite_mutation,
            context_value=self.valid_user_token)
        self.assertEquals(favorite, add_favorite_mutation_response)

    def test_add_favorite_with_empty_title(self):
        """Test adding a favorite thing with empty title."""
        favorite = self.client.execute(
            add_favorite_with_empty_title_mutation,
            context_value=self.valid_user_token)
        self.assertIn("Title cannot be empty", str(favorite))

    def test_add_favorite_with_no_title(self):
        """Test adding a favorite thing with no title."""
        favorite = self.client.execute(
            add_favorite_with_no_title_mutation,
            context_value=self.valid_user_token)
        self.assertIn('\"title\" of type \"String!\" is required but not provided', str(favorite))

    def test_add_favorite_with_no_category_id(self):
        """Test adding a favorite thing with no catgeory id."""
        favorite = self.client.execute(
            add_favorite_with_no_category_id_mutation,
            context_value=self.valid_user_token)
        self.assertIn('\"categoryId\" of type \"Int!\" is required but not provided', str(favorite))

    def test_add_favorite_with_no_ranking(self):
        """Test adding a favorite thing with no ranking."""
        favorite = self.client.execute(
            add_favorite_with_no_ranking_mutation,
            context_value=self.valid_user_token)
        self.assertIn('\"ranking\" of type \"Int!\" is required but not provided', str(favorite))

    def test_add_favorite_with_description_less_than_10_characters(self):
        """Test adding a favorite thing with description less than 10 characters."""
        favorite = self.client.execute(
            add_favorite_with_description_less_than_10_characters,
            context_value=self.valid_user_token)
        self.assertIn('Description must be at least 10 characters', str(favorite))
