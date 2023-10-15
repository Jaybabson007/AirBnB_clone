#!/usr/bin/python3
""" This script defines a class TestUser to test the User module. """

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """This blueprint class defines tests for User Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.user1 = User()
        cls.user1.name = "Joel"

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.user1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.user1)), result)

    def test_inheritance(self):
        """This function tests if User is a subclass and instance of BaseModel.
        """
        self.assertIsInstance(self.user1, User)
        self.assertEqual(type(self.user1), User)
        self.assertEqual(issubclass(self.user1.__class__, BaseModel), True)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.user1.id, str)
        self.assertEqual(type(self.user1.id), str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_functions(self):
        """This function tests if User module is documented.
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """This function tests if expected attributes exist.
        """
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.user1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.user1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.user1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.user1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.user1.id)

    def test_unique_id(self):
        """This function tests if each instance is created with a unique ID.
        """
        user2 = self.user1.__class__()
        user3 = self.user1.__class__()
        user4 = self.user1.__class__()
        self.assertNotEqual(self.user1.id, user2.id)
        self.assertNotEqual(self.user1.id, user3.id)
        self.assertNotEqual(self.user1.id, user4.id)


if __name__ == '__main__':
    unittest.main()
