from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.favorite_things.models import FavoriteThing as FavoriteThingModel
from api.categories.models import Category as CategoryModel
# from api.categories.schema import CategoryResponse


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel


class ReorderFavoriteThings:

    def check_last_favorite_thing_in_category(query, info, user_id, **kwargs):
        query_category = Category.get_query(info)
        category_exists = query_category.filter_by(id=kwargs['category_id']).first()
        if not category_exists:
            raise GraphQLError("Category does not exist")
        last_favorite_thing_in_category = query.filter(
            FavoriteThingModel.user_id == user_id,
            FavoriteThingModel.category_id == kwargs['category_id']
            ).order_by(FavoriteThingModel.ranking.desc()).first()
        if not last_favorite_thing_in_category:
            return 1

        if ('id' in kwargs and last_favorite_thing_in_category
            and kwargs['ranking'] > last_favorite_thing_in_category.ranking): # noqa
            return last_favorite_thing_in_category.ranking

        if ('id' not in kwargs and last_favorite_thing_in_category
            and kwargs['ranking'] > last_favorite_thing_in_category.ranking): # noqa
            return last_favorite_thing_in_category.ranking + 1
        return kwargs['ranking']

    def reorder_favorite_things_on_create(query, user_id, **kwargs):
        query.filter(
                FavoriteThingModel.category_id == kwargs['category_id'],
                FavoriteThingModel.user_id == user_id,
                FavoriteThingModel.ranking >= kwargs['ranking']
                ).update(
                    {FavoriteThingModel.ranking: FavoriteThingModel.ranking + 1},
                    synchronize_session=False)

    def reorder_favorite_things_on_update(query, user_id, favorite_thing, **kwargs):
        if 'id' in kwargs:
            if favorite_thing.ranking < kwargs['ranking']:
                query.filter(
                    FavoriteThingModel.category_id == kwargs['category_id'],
                    FavoriteThingModel.user_id == user_id,
                    FavoriteThingModel.ranking > favorite_thing.ranking,
                    FavoriteThingModel.ranking <= kwargs['ranking'],
                    FavoriteThingModel.id != kwargs['id']
                    ).update(
                        {FavoriteThingModel.ranking: FavoriteThingModel.ranking - 1},
                        synchronize_session=False)
            elif favorite_thing.ranking > kwargs['ranking']:
                query.filter(
                    FavoriteThingModel.category_id == kwargs['category_id'],
                    FavoriteThingModel.user_id == user_id,
                    FavoriteThingModel.ranking < favorite_thing.ranking,
                    FavoriteThingModel.ranking >= kwargs['ranking'],
                    FavoriteThingModel.id != kwargs['id']
                    ).update(
                        {FavoriteThingModel.ranking: FavoriteThingModel.ranking + 1},
                        synchronize_session=False)

    def reorder_favorite_things_on_delete(query, user_id, favorite_thing, **kwargs):
        query.filter(
            FavoriteThingModel.category_id == kwargs['category_id'],
            FavoriteThingModel.user_id == user_id,
            FavoriteThingModel.ranking > favorite_thing.ranking,
            FavoriteThingModel.id != kwargs['id']
            ).update(
                {FavoriteThingModel.ranking: FavoriteThingModel.ranking - 1},
                synchronize_session=False)

    def check_existing_favorite_thing(query, user_id, **kwargs):
        existing_favorite_thing = query.filter(
            FavoriteThingModel.title == kwargs['title'],
            FavoriteThingModel.user_id == user_id,
            FavoriteThingModel.category_id == kwargs['category_id']
            ).first()
        if existing_favorite_thing:
            raise GraphQLError(f"{kwargs['title']} has already been added")
