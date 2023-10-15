#!/usr/bin/python3
"""This python script defines a Base class"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """ The Class that defines the properties of base model """

    def __init__(self, *args, **kwargs):
        """ This function creates new instances of Base """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for (key, value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """This function returns a string represation of class details.

        Returns:
            str: The class details as a string
        """
        string = "["
        string += str(self.__class__.__name__) + '] ('
        string += str(self.id) + ') ' + str(self.__dict__)
        return string

    def save(self):
        """This funcrion updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This function returns a dictionary containing all the key/values pairs
        of __dict__ of the instance.

        Returns:
            dict: returns key/value pairs.
        """
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        return dict_
