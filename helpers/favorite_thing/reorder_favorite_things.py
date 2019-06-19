from graphql import GraphQLError

from api.favorite_things.models import FavoriteThing as FavoriteThingModel


class ReorderFavoriteThings:

    def check_last_favorite_thing_in_category(query, **kwargs):
        last_favorite_thing_in_category = query.filter(
            FavoriteThingModel.user_id == kwargs['user_id'],
            FavoriteThingModel.category_id == kwargs['category_id']
            ).order_by(FavoriteThingModel.ranking.desc()).first()
        if not last_favorite_thing_in_category:
            return 1

        if ('id' not in kwargs and last_favorite_thing_in_category
            and kwargs['ranking'] > last_favorite_thing_in_category.ranking):
            return last_favorite_thing_in_category.ranking + 1
        return kwargs['ranking']

    def reorder_favorite_things_on_create(query, **kwargs):
        favorite_things_in_category = query.filter(
                FavoriteThingModel.category_id == kwargs['category_id'],
                FavoriteThingModel.user_id == kwargs['user_id'],
                FavoriteThingModel.ranking >= kwargs['ranking']
                ).update(
                    {FavoriteThingModel.ranking: FavoriteThingModel.ranking + 1},
                    synchronize_session=False)

    def check_existing_favorite_thing(query, **kwargs):
        existing_favorite_thing = query.filter(
            FavoriteThingModel.title == kwargs['title'],
            FavoriteThingModel.user_id == kwargs['user_id'],
            FavoriteThingModel.category_id == kwargs['category_id']
            ).first()
        if existing_favorite_thing:
            raise GraphQLError(f"{kwargs['title']} has already been added")
