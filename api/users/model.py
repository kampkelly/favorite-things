import os
import sys
from sqlalchemy import Column, String, Integer

sys.path.append(os.getcwd())

from helpers.database import Base # noqa


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
