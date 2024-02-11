#!/usr/bin/python3
"""defines a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """the class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
