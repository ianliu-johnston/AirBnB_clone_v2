#!/usr/bin/python3
"""
City Class:
    Inherits from BaseModel and Base
"""
from models import *


class City(BaseModel, Base):
    """
    Represents Cities available to users
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
