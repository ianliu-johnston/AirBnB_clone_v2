#!/usr/bin/python3
"""
User Class:
    Inherits from BaseModel and Base
"""
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy import Column, String, cascade, backref
from sqlalchemy.orm import relationship


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
