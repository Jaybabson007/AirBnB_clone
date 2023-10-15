#!/usr/bin/python3
"""This python script defines a class State that inherits from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class blueprint that defines the properties of State.

    Attributes:
        name (string): The name of the state.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates new instances of the State class.
        """
        super().__init__(*args, **kwargs)
