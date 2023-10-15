#!/usr/bin/python3
"""This python script defines a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """The  Class that defines the properties of a User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """This function creates new instances of the User class.
        """
        super().__init__(*args, **kwargs)
