import os
import sys
from sqlalchemy import Column, String, Integer, Text, JSON

sys.path.append(os.getcwd())

from helpers.database import Base # noqa


class FavoriteThings(Base):
    __tablename__ = "favorite_things"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=True)
    metadata = Column(JSON(), nullable=True)
    ranking = Column(Integer(), nullable=False)
    category_id = Column(Integer(), nullable=False)
    user_id = Column(Integer(), nullable=False)
