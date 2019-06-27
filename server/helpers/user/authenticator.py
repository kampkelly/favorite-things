import os
import jwt
from functools import wraps
from graphql import GraphQLError


class Authenticator:

    @staticmethod
    def generate_token(id, name, email):
        token = jwt.encode(
            {"id": id, "name": name, "email": email, 'exp': os.getenv('JWT_EXP')},
            os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')
        return token

    def authenticate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.getenv('APP_SETTINGS') == 'testing':
                if 'Access-Token' in args[1].context:
                    token = args[1].context['Access-Token']
                    try:
                        decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                    except jwt.ExpiredSignatureError:
                        raise GraphQLError('Access Token has expired')
                    except jwt.exceptions.DecodeError:
                        raise GraphQLError('Access Token is invalid')
                    args[1].context['user'] = decoded
                else:
                    raise GraphQLError('Access Token is empty')
            else:
                if 'Access-Token' in args[1].context.headers:
                    token = args[1].context.headers['Access-Token']
                    try:
                        decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                    except jwt.ExpiredSignatureError:
                        raise GraphQLError('Access Token has expired')
                    except jwt.exceptions.DecodeError:
                        raise GraphQLError('Access Token is invalid')
                    args[1].context.user = decoded
                else:
                    raise GraphQLError('Access Token is empty')
            return func(*args, **kwargs)
        return wrapper
