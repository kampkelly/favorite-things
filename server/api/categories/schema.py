import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import Category as CategoryModel
from api.favorite_things.models import FavoriteThing as FavoriteThingModel
from api.favorite_things.schema import FavoriteThing
from helpers.user.authenticator import Authenticator
from helpers.audit.add_audit import AddAudit


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel


class FavoritesResponse(SQLAlchemyObjectType):
    class Meta:
        model = FavoriteThingModel


class CategoryResponse(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    favorite_things = graphene.List(FavoritesResponse)


class Query(graphene.ObjectType):
    all_categories = graphene.List(Category)
    get_categories_and_favorites = graphene.List(CategoryResponse)

    def resolve_all_categories(self, info, **kwargs):
        query = Category.get_query(info)
        try:
            categories = query.order_by(CategoryModel.id).all()
        except:
            raise GraphQLError('Server Error')
        return categories

    @Authenticator.authenticate
    def resolve_get_categories_and_favorites(self, info, **kwargs):
        user = info.context.user
        query = Category.get_query(info)
        query_favorite_things = FavoriteThing.get_query(info)
        try:
            categories = query.order_by(CategoryModel.id).all()
            category_responses = []
            for category in categories:
                favorites = query_favorite_things.filter(
                    FavoriteThingModel.user_id == user['id'],
                    FavoriteThingModel.category_id == category.id).order_by(
                        FavoriteThingModel.ranking).all()
                if not len(favorites):
                    continue
                category_response = CategoryResponse(id=category.id, name=category.name, favorite_things=favorites)
                category_responses.append(category_response)
        except:
            raise GraphQLError('Server Error')
        return category_responses


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(Category)

    @Authenticator.authenticate
    def mutate(self, info, name):
        query = Category.get_query(info)
        if not len(name.strip()):
            raise GraphQLError("Category name cannot be empty")
        try:
            existing_category = query.filter(CategoryModel.name == name).first()
            if existing_category:
                raise GraphQLError("Category already exists")
            category = CategoryModel(name=name)
            category.save()
            user = info.context.user
            AddAudit.add_audit(f"You created a category: '{category.name}'", user)
        except:
            raise GraphQLError('Server Error')
        return CreateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    category = graphene.Field(Category)

    @Authenticator.authenticate
    def mutate(self, info, **kwargs):
        query = Category.get_query(info)
        query_favorite_things = FavoriteThing.get_query(info)
        try:
            category = query.filter_by(id=kwargs['id']).first()
            if category:
                has_favorite_things = query_favorite_things.filter(
                    FavoriteThingModel.category_id == category.id).all()
                if has_favorite_things:
                    raise GraphQLError("Cannot delete category because it has favorite things")
                user = info.context.user
                AddAudit.add_audit(f"You deleted the category: '{category.name}'", user)
                category.delete()
            else:
                raise GraphQLError("Category does not exist")
        except:
            raise GraphQLError('Server Error')
        return DeleteCategory(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    delete_category = DeleteCategory.Field()
