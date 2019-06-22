import graphene
from api.users.schema import Query as UserQuery, Mutation as UserMutation
from api.categories.schema import Query as CategoryQuery, Mutation as CategoryMutation
from api.favorite_things.schema import Query as FavoriteThingQuery, Mutation as FavoriteThingMutation
from api.audit.schema import Query as AuditQuery


class Query(UserQuery, CategoryQuery, FavoriteThingQuery, AuditQuery):
    pass


class Mutation(UserMutation, CategoryMutation, FavoriteThingMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
