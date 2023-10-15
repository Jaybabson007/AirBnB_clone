#!/usr/bin/python3
"""This python script defines a class City that inherits from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class blueprint that defines the properties of City.

    Attributes:
        name (string): The name of the city.
        state_id (string): The id of state.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates new instances of City.
        """
        super().__init__(*args, **kwargs)
