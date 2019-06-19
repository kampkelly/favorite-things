import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import FavoriteThing as FavoriteThingModel
from helpers.favorite_thing.validations import FavoriteThingValidations
from helpers.favorite_thing.reorder_favorite_things import ReorderFavoriteThings
from helpers.user.authenticator import Authenticator
from helpers.database import update_entity_fields


class FavoriteThing(SQLAlchemyObjectType):
    class Meta:
        model = FavoriteThingModel


class Query(graphene.ObjectType):
    get_favorite_things = graphene.List(FavoriteThing)

    @Authenticator.authenticate
    def resolve_get_favorite_things(self, info, **kwargs):
        query = FavoriteThing.get_query(info)
        favorite_things = query.filter(
            FavoriteThingModel.user_id == kwargs['user_id']).order_by(
                FavoriteThingModel.ranking).all()
        return favorite_things


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


class UpdateFavoriteThing(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        object_metadata = graphene.JSONString(required=False)
        ranking = graphene.Int(required=True)
        category_id = graphene.Int(required=False)
    favorite_thing = graphene.Field(FavoriteThing)

    @FavoriteThingValidations.input_validation
    @Authenticator.authenticate
    def mutate(self, info, **kwargs):
        query = FavoriteThing.get_query(info)
        favorite_thing = query.filter(
            FavoriteThingModel.id == kwargs['id'],
            FavoriteThingModel.user_id == kwargs['user_id']).first()
        if not favorite_thing:
            raise GraphQLError('Favorite thing does not exist')
        kwargs['category_id'] = favorite_thing.category_id

        kwargs['ranking'] = ReorderFavoriteThings.check_last_favorite_thing_in_category(query, **kwargs)

        ReorderFavoriteThings.reorder_favorite_things_on_update(query, **kwargs)

        update_entity_fields(favorite_thing, **kwargs)
        favorite_thing.save()
        return UpdateFavoriteThing(favorite_thing=favorite_thing)


class Mutation(graphene.ObjectType):
    add_favorite_thing = AddFavoriteThing.Field()
    update_favorite_thing = UpdateFavoriteThing.Field()
