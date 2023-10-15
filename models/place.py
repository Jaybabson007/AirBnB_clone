#!/usr/bin/python3
"""This python script defines a class Place that inherits from BaseModel"""

from models.base_model import BaseModel

class Place(BaseModel):
    """The Class blueprint that defines properties of Place.

    Attributes:
        city_id (string): unique id of city.
        user_id (string): unique id of user.
        name (string): The name of Place.
        description (string): The description of place.
        number_rooms (integer): The number of rooms in place.
        number_bathrooms (integer): The number of bathrooms in place.
        max_guest (integer): The maximum number of guests allowed in a place.
        price_by_night (integer): The price of room per night.
        latitude (float): The latitude of place on a map.
        longitude (float): The longitude of place on a map.
        amenity_ids (list (of string)): The list of Amenity.id of place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """This function creates new instances of the 'Place' class.
        """
        super().__init__(*args, **kwargs)
