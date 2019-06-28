from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

from config import config


config_name = os.getenv('APP_SETTINGS')
database_uri = config.get(config_name).SQLALCHEMY_DATABASE_URI
engine = create_engine(database_uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Utility(object):
    """A class to modify the database."""
    def save(self):
        """Method for saving data"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Method for deleting objects"""
        db_session.delete(self)
        db_session.commit()


def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity
