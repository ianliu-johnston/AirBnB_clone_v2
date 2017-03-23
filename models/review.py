#!/usr/bin/python3
"""
Review Class:
    inherits from Basemodel and Base
"""
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.state import State
from models.user import User
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Represents user reviews
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    """
    Initializes the class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
