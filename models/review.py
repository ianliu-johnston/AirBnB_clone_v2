#!/usr/bin/python3
"""
Review Class:
    inherits from Basemodel and Base
"""
from models import *


class Review(BaseModel):
    """
    Represents user reviews
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))

    """
    Initializes the class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
