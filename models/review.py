#!/usr/bin/python3
"""defines the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Amenity"""
    place_id = ""
    user_id = ""
    text = ""
