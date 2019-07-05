from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from functools import wraps
from dataclasses import dataclass

from api.models import FavoriteThing as FavoriteThingModel
from api.models import Category as CategoryModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel


class FavoriteThing(SQLAlchemyObjectType):
    class Meta:
        model = FavoriteThingModel


@dataclass
class ReorderFavoriteThings:
    """A class to reorder favorite things when creating,
        updating or deleting
    """
    @staticmethod
    def get_user_info_query_variables(args):
        """
        A method to return the info, query and user objects

        Args:
            args (list): A list containing user, info and query

        Returns:
            tuple: Info user and query
        """
        info = args[1]
        user = info.context.user
        query = FavoriteThing.get_query(info)
        return (info, user, query)

    def check_last_favorite_thing_in_category(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            query_category = Category.get_query(info)
            try:
                category_exists = query_category.filter_by(
                    id=kwargs['category_id']
                ).first()
                if not category_exists:
                    raise GraphQLError("Category does not exist")
                last_favorite_thing_in_category = query.filter(
                    FavoriteThingModel.user_id == user['id'],
                    FavoriteThingModel.category_id == kwargs['category_id']
                ).order_by(FavoriteThingModel.ranking.desc()).first()
                if not last_favorite_thing_in_category:
                    kwargs['ranking'] = 1

                if ('id' in kwargs and last_favorite_thing_in_category
                    and kwargs['ranking'] > last_favorite_thing_in_category.ranking): # noqa
                    kwargs['ranking'] = last_favorite_thing_in_category.ranking

                if ('id' not in kwargs and last_favorite_thing_in_category
                    and kwargs['ranking'] > last_favorite_thing_in_category.ranking): # noqa
                    kwargs['ranking'] = last_favorite_thing_in_category.ranking + 1 # noqa
            except:
                raise GraphQLError('Something went wrong. Please try again!')
            return func(*args, **kwargs)
        return wrapper

    def reorder_favorite_things_on_create(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            try:
                query.filter(
                    FavoriteThingModel.category_id == kwargs['category_id'],
                    FavoriteThingModel.user_id == user['id'],
                    FavoriteThingModel.ranking >= kwargs['ranking']
                ).update(
                    {FavoriteThingModel.ranking: FavoriteThingModel.ranking + 1}, # noqa
                    synchronize_session=False)
            except:
                raise GraphQLError('Something went wrong. Please try again!')
            return func(*args, **kwargs)
        return wrapper

    def reorder_favorite_things_on_update(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            if 'id' in kwargs:
                favorite_thing = kwargs['favorite_thing']
                try:
                    if favorite_thing.ranking < kwargs['ranking']:
                        query.filter(
                            FavoriteThingModel.category_id == kwargs['category_id'], # noqa
                            FavoriteThingModel.user_id == user['id'],
                            FavoriteThingModel.ranking > favorite_thing.ranking,
                            FavoriteThingModel.ranking <= kwargs['ranking'],
                            FavoriteThingModel.id != kwargs['id']
                        ).update(
                            {FavoriteThingModel.ranking: FavoriteThingModel.ranking - 1}, # noqa
                            synchronize_session=False)
                    elif favorite_thing.ranking > kwargs['ranking']:
                        query.filter(
                            FavoriteThingModel.category_id == kwargs['category_id'], # noqa
                            FavoriteThingModel.user_id == user['id'],
                            FavoriteThingModel.ranking < favorite_thing.ranking,
                            FavoriteThingModel.ranking >= kwargs['ranking'],
                            FavoriteThingModel.id != kwargs['id']
                        ).update(
                            {FavoriteThingModel.ranking: FavoriteThingModel.ranking + 1}, # noqa
                            synchronize_session=False)
                except:
                    raise GraphQLError('Something went wrong. Please try again!') # noqa
            return func(*args, **kwargs)
        return wrapper

    def reorder_favorite_things_on_delete(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            try:
                favorite_thing = kwargs['favorite_thing']
                query.filter(
                    FavoriteThingModel.category_id == kwargs['category_id'],
                    FavoriteThingModel.user_id == user['id'],
                    FavoriteThingModel.ranking > favorite_thing.ranking,
                    FavoriteThingModel.id != kwargs['id']
                ).update(
                    {FavoriteThingModel.ranking: FavoriteThingModel.ranking - 1}, # noqa
                    synchronize_session=False)
            except:
                raise GraphQLError('Something went wrong. Please try again!')
            return func(*args, **kwargs)
        return wrapper

    def check_existing_favorite_thing(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            try:
                existing_favorite_thing = query.filter(
                    FavoriteThingModel.title == kwargs['title'],
                    FavoriteThingModel.user_id == user['id'],
                    FavoriteThingModel.category_id == kwargs['category_id']
                ).first()
            except:
                raise GraphQLError('Something went wrong. Please try again!')
            if existing_favorite_thing:
                raise GraphQLError(f"{kwargs['title']} has already been added")
            return func(*args, **kwargs)
        return wrapper

    def check_if_favorite_thing_exists(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info, user, query = ReorderFavoriteThings.\
                get_user_info_query_variables(args)
            try:
                favorite_thing = query.filter(
                    FavoriteThingModel.id == kwargs['id'],
                    FavoriteThingModel.user_id == user['id']).first()
            except:
                raise GraphQLError('Something went wrong. Please try again!')
            if not favorite_thing:
                raise GraphQLError('Favorite thing does not exist')
            kwargs['category_id'] = favorite_thing.category_id
            kwargs['favorite_thing'] = favorite_thing
            return func(*args, **kwargs)
        return wrapper

    def __str__(self):
        """Return description of favorite class."""
        return "A class to perform operations on favorite things"
