#!/usr/bin/python3
"""defines a class FileStorage"""

import json
from models.base_model import BaseModel

class FileStorage:
    """storing"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionnary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict2 = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict2, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                dict2 = json.load(f)
                for ob in dict2.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name)(**ob))
        except FileNotFoundError:
            return
