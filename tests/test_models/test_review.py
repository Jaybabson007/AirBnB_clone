#!/usr/bin/python3
""" This script defines a class TestReview to test the Review module. """

import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """This function defines tests for Review Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.review1 = Review()
        cls.review1.name = "Nairobi"

    @classmethod
    def tearDown(cls):
        """This functon cleans up after each test.
        """
        del cls.review1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.review1)), result)

    def test_inheritance(self):
        """This function tests if Review is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.review1, Review)
        self.assertEqual(type(self.review1), Review)
        self.assertEqual(issubclass(self.review1.__class__, BaseModel), True)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.review1.id, str)
        self.assertEqual(type(self.review1.id), str)
        self.assertIsInstance(self.review1.created_at, datetime.datetime)
        self.assertIsInstance(self.review1.updated_at, datetime.datetime)
        self.assertIsInstance(self.review1.text, str)
        self.assertIsInstance(self.review1.place_id, str)
        self.assertIsInstance(self.review1.user_id, str)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_functions(self):
        """This function tests if the Review module is documented.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """This function tests if expected attributes exist.
        """
        self.assertTrue(hasattr(self.review1, 'id'))
        self.assertTrue(hasattr(self.review1, 'created_at'))
        self.assertTrue(hasattr(self.review1, 'updated_at'))
        self.assertTrue(hasattr(self.review1, 'user_id'))
        self.assertTrue(hasattr(self.review1, 'text'))
        self.assertTrue(hasattr(self.review1, 'place_id'))

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.review1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.review1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.review1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.review1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.review1.id)

    def test_unique_id(self):
        """This function tests if each instance is created with a unique ID.
        """
        review2 = self.review1.__class__()
        review3 = self.review1.__class__()
        review4 = self.review1.__class__()
        self.assertNotEqual(self.review1.id, review2.id)
        self.assertNotEqual(self.review1.id, review3.id)
        self.assertNotEqual(self.review1.id, review4.id)


if __name__ == '__main__':
    unittest.main()
