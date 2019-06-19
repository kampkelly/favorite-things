import graphene
from api.users.schema import Query as UserQuery, Mutation as UserMutation
from api.categories.schema import Query as CategoryQuery, Mutation as CategoryMutation
from api.favorite_things.schema import Query as FavoriteThingQuery, Mutation as FavoriteThingMutation


class Query(UserQuery, CategoryQuery, FavoriteThingQuery):
    pass


class Mutation(UserMutation, CategoryMutation, FavoriteThingMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
