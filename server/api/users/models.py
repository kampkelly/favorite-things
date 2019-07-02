from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from helpers.database import Base, Utility
from api.audit.models import Audit # noqa


class User(Base, Utility):
    """
    An class used to represent the User model

    Args:
        Base (class): A Base class for sqlalchemy
        Utility (class): A class to save and update records
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    audit_logs = relationship("Audit")
