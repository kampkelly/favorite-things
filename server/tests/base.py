import os
import jwt
from alembic import command, config
from flask_testing import TestCase
from flask_bcrypt import Bcrypt
from graphene.test import Client
from app_config import create_app
from schema import schema
from api.categories.models import Category
from api.users.models import User
from api.favorite_things.models import FavoriteThing
from helpers.database import Base, engine, db_session
# from helpers.audit.add_audit import AddAudit


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        """Creates the app."""
        app = create_app('testing')
        self.client = Client(schema)
        return app

    def setUp(self):
        """Setup the app with database."""
        app = self.create_app()
        bcrypt = Bcrypt(app)
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            try:
                command.stamp(self.alembic_configuration, 'head')
                command.downgrade(self.alembic_configuration, '-1')
                command.upgrade(self.alembic_configuration, 'head')
            except: # noqa
                command.rollback()

            category1 = Category(name="person")
            category1.save()
            category2 = Category(name="place")
            category2.save()
            category3 = Category(name="food")
            category3.save()

            password = bcrypt.generate_password_hash('password').decode('utf-8')
            user = User(email="runor@example.com", name="Runor", password=password)
            user.save()

            favorite = FavoriteThing(title="Football", ranking=1, category_id=1, user_id=1)
            favorite.save()

            # AddAudit.add_audit(
            # f"You added a new favorite thing: '{favorite.title}'\
            # with ranking of '{favorite.ranking}'", user)

        self.expired_token = jwt.encode(
            {"id": 1, "name": 'Runor', "email": 'runor@example.com'},
            os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')

        self.token = jwt.encode(
            {"id": 1, "name": 'Runor', "email": 'runor@example.com', 'exp': 1371720939},
            os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')

    def tearDown(self):
        """Teardown the app and drop all databases."""
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
