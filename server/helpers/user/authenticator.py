import os
import jwt
from functools import wraps
from graphql import GraphQLError
from flask import jsonify


class Authenticator:
    """A class to perform authentication a user."""

    @staticmethod
    def generate_token(id, name, email):
        """A methid to generate user token."""
        token = jwt.encode(
            {"id": id, "name": name, "email": email, 'exp': os.getenv('JWT_EXP')},
            os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')
        return token

    def authenticate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.getenv('APP_SETTINGS') == 'testing':
                if 'user-key' in args[1].context:
                    user_key = args[1].context['user-key']
                    if user_key.split(' ')[0] != 'Bearer':
                        raise GraphQLError('Invalid token supplied')
                    try:
                        token = user_key.split(' ')[1]
                        decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                    except jwt.ExpiredSignatureError:
                        raise GraphQLError('Authorization code has expired')
                    except jwt.exceptions.DecodeError:
                        raise GraphQLError('Invalid token supplied')
                    args[1].context = jsonify(args[1].context)
                    args[1].context.user = decoded
                else:
                    raise GraphQLError('Authorization code is empty')
            else:
                if 'user-key' in args[1].context.headers:
                    user_key = args[1].context.headers['user-key']
                    if user_key.split(' ')[0] != 'Bearer':
                        raise GraphQLError('Invalid token supplied')
                    try:
                        token = user_key.split(' ')[1]
                        decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                    except jwt.ExpiredSignatureError:
                        raise GraphQLError('Authorization code has expired')
                    except jwt.exceptions.DecodeError:
                        raise GraphQLError('Invalid token supplied')
                    args[1].context.user = decoded
                else:
                    raise GraphQLError('Authorization code is empty')
            return func(*args, **kwargs)
        return wrapper
