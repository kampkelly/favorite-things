from sqlalchemy import Column, String, Integer

from helpers.database import Base, Utility


class User(Base, Utility):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
