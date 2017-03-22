#!/usr/bin/python3
"""
State Class:
    Inherits from BaseModel and Base
"""
from models import *


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
