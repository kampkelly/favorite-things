import os
import sys
from sqlalchemy import Column, String, Integer, Text, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

sys.path.append(os.getcwd())

from helpers.database import Base, Utility # noqa


class FavoriteThing(Base, Utility):
    __tablename__ = "favorite_things"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=True)
    object_metadata = Column("metadata", JSON(), nullable=True)
    ranking = Column(Integer(), nullable=False)
    category_id = Column(Integer(), ForeignKey('categories.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now(timezone="WAT"), nullable=False)
    category = relationship("Category")
    user = relationship("User")
