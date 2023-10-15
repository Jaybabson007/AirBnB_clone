#!/usr/bin/python3
"""This python script defines a class TestAmenity
to test the Amenity module. """

import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """This blueprint class defines tests for Amenity Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Parking"

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.amenity1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity1)), result)

    def test_inheritance(self):
        """This function tests if Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.amenity1, Amenity)
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertEqual(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.amenity1.name, str)
        self.assertEqual(type(self.amenity1.name), str)
        self.assertIsInstance(self.amenity1.id, str)
        self.assertEqual(type(self.amenity1.id), str)
        self.assertIsInstance(self.amenity1.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity1.updated_at, datetime.datetime)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_functions(self):
        """This function tests if Amenity module is documented.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """This function tests if expected attributes exist.
        """
        self.assertTrue(hasattr(self.amenity1, 'name'))
        self.assertTrue(hasattr(self.amenity1, 'id'))
        self.assertTrue(hasattr(self.amenity1, 'created_at'))
        self.assertTrue(hasattr(self.amenity1, 'updated_at'))

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.amenity1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.amenity1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.amenity1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.amenity1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.amenity1.id)

    def test_unique_id(self):
        """This functiion Tests if each instance is created with a unique ID.
        """
        amenity2 = self.amenity1.__class__()
        amenity3 = self.amenity1.__class__()
        amenity4 = self.amenity1.__class__()
        self.assertNotEqual(self.amenity1.id, amenity2.id)
        self.assertNotEqual(self.amenity1.id, amenity3.id)
        self.assertNotEqual(self.amenity1.id, amenity4.id)


if __name__ == '__main__':
    unittest.main()
