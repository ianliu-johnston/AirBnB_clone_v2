#!/usr/bin/python3
"""
State Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models import storage
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
        @property
        def cities(self):
            stor = storage.all('City').values()
            return ([a for a in stor if self.id == a.state_id])
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
