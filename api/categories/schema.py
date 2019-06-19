import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import Category as CategoryModel
from api.favorite_things.models import FavoriteThing as FavoriteThingModel
from api.favorite_things.schema import FavoriteThing
from helpers.user.authenticator import Authenticator


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
    get_categories = graphene.List(Category)
    get_categories_and_favorites = graphene.List(CategoryResponse)

    def resolve_get_categories(self, info, **kwargs):
        query = Category.get_query(info)
        categories = query.order_by(CategoryModel.id).all()
        return categories

    @Authenticator.authenticate
    def resolve_get_categories_and_favorites(self, info, **kwargs):
        query = Category.get_query(info)
        query_favorite_things = FavoriteThing.get_query(info)
        categories = query.order_by(CategoryModel.id).all()
        category_responses = []
        for category in categories:
            favorites = query_favorite_things.filter(
                FavoriteThingModel.user_id == kwargs['user_id'],
                FavoriteThingModel.category_id == category.id).order_by(
                    FavoriteThingModel.ranking).all()
            if not len(favorites):
                continue
            category_response = CategoryResponse(id=category.id, name=category.name, favorite_things=favorites)
            category_responses.append(category_response)
        return category_responses


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(Category)

    def mutate(self, info, name):
        query = Category.get_query(info)
        if len(name) < 2:
            raise GraphQLError("Category name must be up to 2 characters")
        existing_category = query.filter(CategoryModel.name == name).first()
        if existing_category:
            raise GraphQLError("Category already exists")
        category = CategoryModel(name=name)
        category.save()
        return CreateCategory(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
