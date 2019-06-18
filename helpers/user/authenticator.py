import os
import jwt


class Authenticator:

    def generate_token(name, email):
        token = jwt.encode(
            {"name": name, "email": email},
            os.getenv('JWT_SECRET'), algorithm='HS256')
        return token
