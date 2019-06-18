from alembic import command, config
from flask_testing import TestCase
from graphene.test import Client
from app_config import create_app
from schema import schema
from api.categories.models import Category
from helpers.database import Base, engine, db_session


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        app = create_app('testing')
        # self.base_url = "http://0.0.0.0:4000/demo_app"
        # self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)

            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')

            category1 = Category(name="person")
            category1.save()
            category2 = Category(name="place")
            category2.save()
            category3 = Category(name="food")
            category3.save()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
