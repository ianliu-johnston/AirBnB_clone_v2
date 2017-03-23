#!/usr/bin/python3
"""
Review Class:
    inherits from Basemodel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """
    Represents user reviews
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),
                      ForeignKey("places.id"),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id"),
                     nullable=False)

    """
    Initializes the class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
