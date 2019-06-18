import graphene
from api.users.schema import Query as UserQuery, Mutation as UserMutation
from api.categories.schema import Query as CategoryQuery, Mutation as CategoryMutation


class Query(UserQuery, CategoryQuery):
    pass


class Mutation(UserMutation, CategoryMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
