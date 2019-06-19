import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import FavoriteThing as FavoriteThingModel
from helpers.favorite_thing.validations import FavoriteThingValidations
from helpers.favorite_thing.reorder_favorite_things import ReorderFavoriteThings
from helpers.user.authenticator import Authenticator


class FavoriteThing(SQLAlchemyObjectType):
    class Meta:
        model = FavoriteThingModel
        only_fields = ("id", "title", "description", "object_metadata", "ranking", "category_id", "user_id", "created_date")


class Query(graphene.ObjectType):
    get_favorite_things = graphene.Field(FavoriteThing)

    def resolve_get_favorite_things(self, info, **kwargs):
        query = FavoriteThing.get_query(info)
        return query


class AddFavoriteThing(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)
        object_metadata = graphene.JSONString(required=False)
        ranking = graphene.Int(required=True)
        category_id = graphene.Int(required=True)
    favorite_thing = graphene.Field(FavoriteThing)

    @FavoriteThingValidations.input_validation
    @Authenticator.authenticate
    def mutate(self, info, **kwargs):
        query = FavoriteThing.get_query(info)
        ReorderFavoriteThings.check_existing_favorite_thing(query, **kwargs)

        kwargs['ranking'] = ReorderFavoriteThings.check_last_favorite_thing_in_category(
            query, **kwargs)

        ReorderFavoriteThings.reorder_favorite_things_on_create(query, **kwargs)

        favorite_thing = FavoriteThingModel(**kwargs)
        favorite_thing.save()
        return AddFavoriteThing(favorite_thing=favorite_thing)


class Mutation(graphene.ObjectType):
    add_favorite_thing = AddFavoriteThing.Field()
