import datetime
from functools import wraps
from graphql import GraphQLError


class FavoriteThingValidations:
    """
    Validate favorite thing entries
    
    Raises:
        GraphQLError: Raises an error if validation fails
    
    Returns:
        function: The passed in function
    """
    def input_validation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors = []
            if 'title' in kwargs:
                kwargs['title'] = kwargs['title'].strip()
                if not len(kwargs['title']):
                    errors.append("Title cannot be empty")
            if kwargs['ranking'] < 1:
                errors.append("Ranking must be greater than 0")
            if 'description' in kwargs and kwargs['description'] != '' and len(kwargs['description']) < 10:
                kwargs['description'] = kwargs['description'].strip()
                errors.append("Description must be at least 10 characters")
            if 'object_metadata' in kwargs:
                for field in kwargs['object_metadata']:
                    value = kwargs['object_metadata'].get(field)
                    value_type = isinstance(value, (str, int, datetime.datetime))
                    if not value_type:
                        errors.append('Metadata only allows text, number, date, or enum values')
            if len(errors):
                raise GraphQLError(
                    ('The following errors occured: {}').format(str(errors).strip('[]'))
                )
            return func(*args, **kwargs)
        return wrapper
