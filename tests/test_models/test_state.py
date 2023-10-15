#!/usr/bin/python3
""" This script defines a class TestState to test the State module. """

import unittest
import datetime
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """This blueprint class defines tests for State Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.state1 = State()
        cls.state1.name = "Abuja"

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.state1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state1)), result)

    def test_inheritance(self):
        """This function tests if State is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.state1, State)
        self.assertEqual(type(self.state1), State)
        self.assertEqual(issubclass(self.state1.__class__, BaseModel), True)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.state1.id, str)
        self.assertEqual(type(self.state1.id), str)
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)
        self.assertIsInstance(self.state1.name, str)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_functions(self):
        """This function tests if State module is documented.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """This function tests if expected attributes exist.
        """
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))
        self.assertTrue(hasattr(self.state1, 'name'))

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.state1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.state1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.state1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.state1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.state1.id)

    def test_unique_id(self):
        """This function tests if each instance is created with a unique ID.
        """
        state2 = self.state1.__class__()
        state3 = self.state1.__class__()
        state4 = self.state1.__class__()
        self.assertNotEqual(self.state1.id, state2.id)
        self.assertNotEqual(self.state1.id, state3.id)
        self.assertNotEqual(self.state1.id, state4.id)


if __name__ == '__main__':
    unittest.main()
