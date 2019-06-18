import re
from functools import wraps
from graphql import GraphQLError

email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"


class UserValidations:
    """ Validate user entries for signup and signin
    :methods
        signup_validation
    """

    def input_validation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors = []
            for field in kwargs:
                value = kwargs.get(field)
                value.strip()
            kwargs['email'] = kwargs['email'].replace(" ", "")
            valid_email = re.match(email_pattern, kwargs['email'])
            if not valid_email:
                errors.append('Provided email address is not valid')
            if len(kwargs['password']) < 8:
                errors.append('Password length is too short, it should be up to 8 characters')
            if 'name' in kwargs and len(kwargs['name']) < 3:
                errors.append('Name is too short')
            if len(errors):
                raise GraphQLError(
                    ('The following errors occured: {}').format(str(errors).strip('[]'))
                )
            return func(*args, **kwargs)
        return wrapper
