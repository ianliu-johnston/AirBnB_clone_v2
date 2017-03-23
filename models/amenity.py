#!/usr/bin/python3
"""
Amenity Class:
    Inherits from BaseModel and Base, defines two new class attributes
"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
#from models.city import City
from models.__init__ import storage
#from models.place import Place
#from models.review import Review
#from models.state import State
#from models.user import User
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    """
    Initializes the class with args and kwargs
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
