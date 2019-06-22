import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app_config import bcrypt
from .models import User as UserModel
from helpers.user.validations import UserValidations
from helpers.user.authenticator import Authenticator


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        only_fields = ("name", "email", "audit_logs")


class Query(graphene.ObjectType):
    get_user_details = graphene.Field(User)

    @Authenticator.authenticate
    def resolve_get_user_details(self, info, **kwargs):
        user_id = info.context.user['id']
        query = User.get_query(info)
        user = query.filter_by(id=user_id).first()
        return user


class SignupUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(User)
    token = graphene.String()

    @UserValidations.input_validation
    def mutate(self, info, **kwargs):
        kwargs['password'] = bcrypt.generate_password_hash(kwargs['password']).decode('utf-8')
        query = User.get_query(info)
        existing_user = query.filter(UserModel.email == kwargs['email']).first()
        if existing_user:
            raise GraphQLError("An account with this email already exists")
        user = UserModel(**kwargs)
        user.save()
        token = Authenticator.generate_token(user.id, kwargs['name'], kwargs['email'])
        return SignupUser(user=user, token=token)


class SigninUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(User)
    token = graphene.String()

    @UserValidations.input_validation
    def mutate(self, info, **kwargs):
        query = User.get_query(info)
        user = query.filter(UserModel.email == kwargs['email']).first()
        if user:
            check_password = bcrypt.check_password_hash(user.password, kwargs['password'])
            if check_password:
                token = Authenticator.generate_token(user.id, user.name, user.email)
                return SignupUser(user=user, token=token)
            else:
                raise GraphQLError("Email or password is incorrect")
        else:
            raise GraphQLError("Email or password is incorrect")


class Mutation(graphene.ObjectType):
    signup_user = SignupUser.Field()
    signin_user = SigninUser.Field()
