import os
import sys
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql import func

sys.path.append(os.getcwd())

from helpers.database import Base, Utility # noqa


class Category(Base, Utility):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.now(timezone="WAT"), nullable=False)
