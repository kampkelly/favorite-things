import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import Category as CategoryModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        only_fields = ("id", "name", "created_date")


class Query(graphene.ObjectType):
    get_categories = graphene.List(Category)

    def resolve_get_categories(self, info, **kwargs):
        query = Category.get_query(info)
        categories = query.order_by(CategoryModel.id).all()
        return categories


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
