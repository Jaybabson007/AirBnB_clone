#!/usr/bin/python3
""" This script defines a class TestPlace to test the Place module. """

import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """This class blueprint defines tests for Place Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.place1 = Place()
        cls.place1.name = "Abuja"

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.place1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.place1)), result)

    def test_inheritance(self):
        """This function tests if Place is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.place1, Place)
        self.assertEqual(type(self.place1), Place)
        self.assertEqual(issubclass(self.place1.__class__, BaseModel), True)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.place1.name, str)
        self.assertEqual(type(self.place1.name), str)
        self.assertIsInstance(self.place1.id, str)
        self.assertEqual(type(self.place1.id), str)
        self.assertIsInstance(self.place1.created_at, datetime.datetime)
        self.assertIsInstance(self.place1.updated_at, datetime.datetime)
        self.assertIsInstance(self.place1.amenity_ids, list)
        self.assertIsInstance(self.place1.longitude, float)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.user_id, str)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_functions(self):
        """This function tests if Place module is documented.
        """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """This function tests if expected attributes exist.
        """
        self.assertTrue(hasattr(self.place1, 'name'))
        self.assertTrue(hasattr(self.place1, 'id'))
        self.assertTrue(hasattr(self.place1, 'created_at'))
        self.assertTrue(hasattr(self.place1, 'updated_at'))
        self.assertTrue(hasattr(self.place1, 'city_id'))
        self.assertTrue(hasattr(self.place1, 'user_id'))
        self.assertTrue(hasattr(self.place1, 'description'))
        self.assertTrue(hasattr(self.place1, 'number_rooms'))
        self.assertTrue(hasattr(self.place1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place1, 'max_guest'))
        self.assertTrue(hasattr(self.place1, 'price_by_night'))
        self.assertTrue(hasattr(self.place1, 'latitude'))
        self.assertTrue(hasattr(self.place1, 'longitude'))
        self.assertTrue(hasattr(self.place1, 'amenity_ids'))

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.place1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.place1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.place1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.place1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.place1.id)

    def test_unique_id(self):
        """This function tests if each instance is created with a unique ID.
        """
        place2 = self.place1.__class__()
        place3 = self.place1.__class__()
        place4 = self.place1.__class__()
        self.assertNotEqual(self.place1.id, place2.id)
        self.assertNotEqual(self.place1.id, place3.id)
        self.assertNotEqual(self.place1.id, place4.id)


if __name__ == '__main__':
    unittest.main()
