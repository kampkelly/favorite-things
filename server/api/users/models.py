from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from helpers.database import Base, Utility
from api.audit.models import Audit # noqa


class User(Base, Utility):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    audit_logs = relationship("Audit")
