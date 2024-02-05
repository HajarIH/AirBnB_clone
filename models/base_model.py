#!/usr/bin/python3
"""a module that defines a BaseModel"""

import uuid
from datetime import datetime

class BaseModel:
    """The class BaseModel"""

    def __init__(self):
        """initializes the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "print: [{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
