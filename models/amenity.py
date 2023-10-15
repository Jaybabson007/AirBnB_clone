#!/usr/bin/python3
"""This python script defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Class blueprint that defines properties of Amenity.

    Attributes:
        name (string): The name of amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates new instances of the Amenity class.
        """
        super().__init__(*args, **kwargs)
