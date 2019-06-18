import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app_config import bcrypt
from .models import Category as CategoryModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        only_fields = ("name", "email")


class Query(graphene.ObjectType):
    get_categories = graphene.Field(Category)

    def resolve_get_categories(self, info, email):
        query = Category.get_query(info)
        return query


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
