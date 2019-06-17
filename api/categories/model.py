import os
import sys
from sqlalchemy import Column, String, Integer

sys.path.append(os.getcwd())

from helpers.database import Base # noqa


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    category = Column(String(255), nullable=False)
