#!/usr/bin/python3
"""
City Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from models.__init__ import storage
from models.state import State
from models.user import User
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """
    Represents Cities available to users
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
