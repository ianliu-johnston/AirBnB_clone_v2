#!/usr/bin/python3
"""
User Class:
    Inherits from BaseModel and Base
"""
from models import *


class User(BaseModel):
    """
    Represents users themselves, with personal information
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
