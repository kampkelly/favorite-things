import graphene
import jwt
import os
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app_config import bcrypt
from .models import User as UserModel
from helpers.user.validations import UserValidations
from helpers.user.authenticator import Authenticator


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        only_fields = ("name", "email")


class Query(graphene.ObjectType):
    get_user = graphene.Field(User, email=graphene.String(required=True))

    def resolve_get_user(self, info, email):
        query = User.get_query(info)
        return query


class SignupUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(User)
    token = graphene.String()

    @UserValidations.signup_validation
    def mutate(self, info, **kwargs):
        kwargs['password'] = bcrypt.generate_password_hash(kwargs['password']).decode('utf-8')
        query = User.get_query(info)
        existing_user = query.filter(UserModel.email == kwargs['email']).first()
        if existing_user:
            raise GraphQLError("An account with this email already exists")
        user = UserModel(**kwargs)
        user.save()
        token = Authenticator.generate_token(kwargs['name'], kwargs['email'])
        return SignupUser(user=user, token=token)


class Mutation(graphene.ObjectType):
    signup_user = SignupUser.Field()
