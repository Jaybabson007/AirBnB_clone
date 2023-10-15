#!/usr/bin/python3
"""This python script defines a class 
called FileStorage.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class FileStorage():
    """The Class that serializes instances to a JSON file and deserializes
    the JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """This function creates new instances of class.
        """
        pass

    def all(self):
        """This function returns the dictionary objects.

        Returns:
            dict: returns objects.
        """
        return self.__objects

    def new(self, obj):
        """This function Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (any): object.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """This function Serializes __objects into the JSON file (path: __file_path).
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(dictionary, myFile)

    def reload(self):
        """This function deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists, else, it does nothing. If the file doesn’t
        exist, no exception should be raised
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except Exception:
            return
        objects = eval(my_obj_dump)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects

    def delete(self, obj):
        """This function deletes obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False
