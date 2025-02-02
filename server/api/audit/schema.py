import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.models import Audit as AuditModel
from helpers.user.authenticator import Authenticator


class Audit(SQLAlchemyObjectType):
    """
        Autogenerated return type of Audit
    """
    class Meta:
        model = AuditModel


class Query(graphene.ObjectType):
    """
    Query to return the Audit data

    Args:
        graphene (ObjectType): The graphene object

    Raises:
        GraphQLError: Raises an error when it occurs

    Returns:
        [Object]: Audit data
    """
    get_user_logs = graphene.List(Audit)

    @Authenticator.authenticate
    def resolve_get_user_logs(self, info, **kwargs):
        """Returns the user logs."""
        user = info.context.user
        query = Audit.get_query(info)
        try:
            user_logs = query.filter(
                AuditModel.user_id == user['id']).order_by(
                    AuditModel.id.desc()).all()
        except:
            raise GraphQLError('Something went wrong. Please try again!')
        return user_logs
