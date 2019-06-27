import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from .models import Audit as AuditModel
from helpers.user.authenticator import Authenticator


class Audit(SQLAlchemyObjectType):
    class Meta:
        model = AuditModel


class Query(graphene.ObjectType):
    get_user_logs = graphene.List(Audit)

    @Authenticator.authenticate
    def resolve_get_user_logs(self, info, **kwargs):
        user = info.context.user
        query = Audit.get_query(info)
        try:
            user_logs = query.filter(
                AuditModel.user_id == user['id']).order_by(
                    AuditModel.id.desc()).all()
        except:
            raise GraphQLError('Server Error')
        return user_logs
