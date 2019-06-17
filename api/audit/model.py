import os
import sys
from sqlalchemy import Column, String, Integer

sys.path.append(os.getcwd())

from helpers.database import Base # noqa


class Audit(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    log = Column(String(255), nullable=False)
    user_id = Column(Integer(), nullable=False)
