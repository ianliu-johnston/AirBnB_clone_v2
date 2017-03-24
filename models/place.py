#!/usr/bin/python3
"""
Place Class:
    inherits from base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv

class PlaceAmenity(Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "place_amenity"
        place_id = Column(String(60), ForeignKey("places.id"),
                          nullable=False, primary_key=True)
        amenity_id = Column(String(60), ForeignKey("amenities.id"),
                            nullable=False, primary_key=True)
    else:
        place_id = ""
        amenity_id = ""


class Place(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = [""]
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms =""
        number_bathrooms =""
        max_guest = ""
        price_by_night = ""
        latitude = ""
        longitude = ""
        amenities = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
