#!/usr/bin/python3
"""This python script defines a class Review that inherits from the BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """The Class blueprint that defines properties of Review .

    Attributes:
        place_id (string): unique id of city.
        user_id (string): unique id of user.
        text (string): an empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This function creates new instances of the 'Review' class.
        """
        super().__init__(*args, **kwargs)
