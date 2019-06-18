import os
import sys
from sqlalchemy import Column, String, Integer

sys.path.append(os.getcwd())

from helpers.database import Base, Utility # noqa


class Category(Base, Utility):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
