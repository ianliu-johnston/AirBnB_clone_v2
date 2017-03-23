#!/usr/bin/python3
"""
Amenity Class:
    Inherits from BaseModel and Base, defines two new class attributes
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with args and kwargs
        """
        super().__init__(*args, **kwargs)
