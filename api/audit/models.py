import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

sys.path.append(os.getcwd())

from helpers.database import Base, Utility # noqa


class Audit(Base, Utility):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    log = Column(String(255), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    user = relationship("User")
