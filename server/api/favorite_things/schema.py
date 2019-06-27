import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import FavoriteThing as FavoriteThingModel
from helpers.favorite_thing.validations import FavoriteThingValidations
from helpers.favorite_thing.reorder_favorite_things import ReorderFavoriteThings
from helpers.user.authenticator import Authenticator
from helpers.database import update_entity_fields
from helpers.audit.add_audit import AddAudit


class FavoriteThing(SQLAlchemyObjectType):
    class Meta:
        model = FavoriteThingModel


class Query(graphene.ObjectType):
    get_favorite_things = graphene.List(FavoriteThing)
    get_single_favorite_thing = graphene.Field(FavoriteThing, id=graphene.Int(required=True))

    @Authenticator.authenticate
    def resolve_get_favorite_things(self, info, **kwargs):
        user = info.context.user
        query = FavoriteThing.get_query(info)
        try:
            favorite_things = query.filter(
                FavoriteThingModel.user_id == user['id']).order_by(
                    FavoriteThingModel.ranking).all()
        except:
            raise GraphQLError('Server Error')
        return favorite_things

    @Authenticator.authenticate
    def resolve_get_single_favorite_thing(self, info, id):
        user = info.context.user
        query = FavoriteThing.get_query(info)
        try:
            favorite_thing = query.filter(
                FavoriteThingModel.user_id == user['id'],
                FavoriteThingModel.id == id).first()
        except:
            raise GraphQLError('Server Error')
        if not favorite_thing:
            raise GraphQLError('Favorite thing does not exist')
        return favorite_thing


class AddFavoriteThing(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)
        object_metadata = graphene.JSONString(required=False)
        ranking = graphene.Int(required=True)
        category_id = graphene.Int(required=True)
    favorite_thing = graphene.Field(FavoriteThing)

    @Authenticator.authenticate
    @FavoriteThingValidations.input_validation
    @ReorderFavoriteThings.check_existing_favorite_thing
    @ReorderFavoriteThings.check_last_favorite_thing_in_category
    @ReorderFavoriteThings.reorder_favorite_things_on_create
    def mutate(self, info, **kwargs):
        user = info.context.user
        kwargs['user_id'] = user['id']
        try:
            favorite_thing = FavoriteThingModel(**kwargs)
            favorite_thing.save()
            AddAudit.add_audit(
                f"You added a new favorite thing: '{favorite_thing.title}'\
                with ranking of '{favorite_thing.ranking}'", user)
        except:
            raise GraphQLError('Server Error')
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

    @Authenticator.authenticate
    @FavoriteThingValidations.input_validation
    @ReorderFavoriteThings.check_if_favorite_thing_exists
    @ReorderFavoriteThings.check_last_favorite_thing_in_category
    @ReorderFavoriteThings.reorder_favorite_things_on_update
    def mutate(self, info, **kwargs):
        user = info.context.user
        favorite_thing = kwargs.pop("favorite_thing", None)
        try:
            update_entity_fields(favorite_thing, **kwargs)
            favorite_thing.save()
            AddAudit.add_audit(
                f"You updated the favorite thing: '{favorite_thing.title}'", user)
        except:
            raise GraphQLError('Server Error')
        return UpdateFavoriteThing(favorite_thing=favorite_thing)


class DeleteFavoriteThing(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    favorite_thing = graphene.Field(FavoriteThing)

    @Authenticator.authenticate
    @ReorderFavoriteThings.check_if_favorite_thing_exists
    @ReorderFavoriteThings.reorder_favorite_things_on_delete
    def mutate(self, info, **kwargs):
        user = info.context.user
        favorite_thing = kwargs.pop("favorite_thing", None)
        try:
            favorite_thing.delete()
            AddAudit.add_audit(
                f"You deleted the favorite thing: '{favorite_thing.title}'", user)
        except:
            raise GraphQLError('Server Error')
        return DeleteFavoriteThing(favorite_thing=favorite_thing)


class Mutation(graphene.ObjectType):
    add_favorite_thing = AddFavoriteThing.Field()
    update_favorite_thing = UpdateFavoriteThing.Field()
    delete_favorite_thing = DeleteFavoriteThing.Field()
