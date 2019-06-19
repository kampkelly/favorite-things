import os
import jwt
from functools import wraps
from graphql import GraphQLError


class Authenticator:

    def generate_token(id, name, email):
        token = jwt.encode(
            {"id": id, "name": name, "email": email},
            os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')
        return token

    def authenticate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'Access-Token' in args[1].context.headers:
                token = args[1].context.headers['Access-Token']
                decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                kwargs['user_id'] = decoded['id']
            else:
                raise GraphQLError('Access Token is empty')
            return func(*args, **kwargs)
        return wrapper
