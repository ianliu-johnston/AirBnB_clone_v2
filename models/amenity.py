#!/usr/bin/python3

"""
Amenity Class:
    Inherits from BaseModel and Base, defines two new class attributes
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with args and kwargs
        """
        super().__init__(*args, **kwargs)
