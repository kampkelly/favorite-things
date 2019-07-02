import graphene
import api.users.schema
import api.categories.schema
import api.favorite_things.schema
import api.audit.schema


class Query(
    api.users.schema.Query,
    api.categories.schema.Query,
    api.favorite_things.schema.Query,
    api.audit.schema.Query
):
    pass


class Mutation(
    api.users.schema.Mutation,
    api.categories.schema.Mutation,
    api.favorite_things.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
