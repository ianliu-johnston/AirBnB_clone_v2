#!/usr/bin/python3
"""
User Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """
    Represents users themselves, with personal information
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="delete", backref="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
