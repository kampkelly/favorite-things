import graphene
from api.users.schema import Query as UserQuery, Mutation as UserMutation


class Query(UserQuery):
    pass


class Mutation(UserMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
