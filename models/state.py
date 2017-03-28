#!/usr/bin/python3
"""
State Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv

class State(BaseModel, Base):
    """
    Class to handle state objecs
    Cities and places inherit from this class
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""
        @property
        def cities(self):
            allstorage = storage.all('Cities')
            return (a for a in allstorage)

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
