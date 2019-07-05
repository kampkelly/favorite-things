import os
import sys
from sqlalchemy import Column, String, Integer, Text, ForeignKey, TIMESTAMP, JSON # noqa
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

sys.path.append(os.getcwd())

from helpers.database import Base, Utility # noqa


class Audit(Base, Utility):
    """
    An class used to represent the Audit model

    Args:
        Base (class): A Base class for sqlalchemy
        Utility (class): A class to save and update records
    """
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    log = Column(String(255), nullable=False)
    user_id = Column(Integer(), ForeignKey(
        'users.id',
        ondelete="CASCADE"
    ), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now(
        timezone="WAT"
    ), nullable=False)
    user = relationship("User")


class Category(Base, Utility):
    """
    An class used to represent the Category model

    Args:
        Base (class): A Base class for sqlalchemy
        Utility (class): A class to save and update records
    """
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now(
        timezone="WAT"
    ), nullable=False)


class FavoriteThing(Base, Utility):
    """
    An class used to represent the FavoriteThing model

    Args:
        Base (class): A Base class for sqlalchemy
        Utility (class): A class to save and update records
    """
    __tablename__ = "favorite_things"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=True)
    object_metadata = Column("metadata", JSON(), nullable=True)
    ranking = Column(Integer(), nullable=False)
    category_id = Column(Integer(), ForeignKey(
        'categories.id',
        ondelete="CASCADE"
    ), nullable=False)
    user_id = Column(Integer(), ForeignKey(
        'users.id',
        ondelete="CASCADE"
    ), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now(
        timezone="WAT"
    ), nullable=False)
    category = relationship("Category")
    user = relationship("User")


class User(Base, Utility):
    """
    An class used to represent the User model

    Args:
        Base (class): A Base class for sqlalchemy
        Utility (class): A class to save and update records
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    audit_logs = relationship("Audit")
