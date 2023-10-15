#!/usr/bin/python3
""" This script defines a class TestBaseModel 
to test the  BaseModel module. """

import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """This blueprint class defines tests for Amenity Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.BaseModel1 = BaseModel()
        cls.BaseModel1.name = "Nokia"
        cls.BaseModel1.my_number = 33

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.BaseModel1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.BaseModel1)), result)

    def testBaseModel1(self):
        """This function tests attributes value of a BaseModel instance.
        """
        self.BaseModel1.save()
        my_model_json = self.BaseModel1.to_dict()

        self.assertEqual(self.BaseModel1.name, my_model_json['name'])
        self.assertEqual(self.BaseModel1.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.BaseModel1.id, my_model_json['id'])

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.BaseModel1.name, str)
        self.assertEqual(type(self.BaseModel1.name), str)
        self.assertIsInstance(self.BaseModel1.id, str)
        self.assertEqual(type(self.BaseModel1.id), str)
        self.assertIsInstance(self.BaseModel1.created_at, datetime.datetime)
        self.assertIsInstance(self.BaseModel1.updated_at, datetime.datetime)

    def test_save(self):
        """This function tests if save method is working correctly after update.
        """
        self.BaseModel1.save()
        self.assertNotEqual(self.BaseModel1.created_at,
                            self.BaseModel1.updated_at)

    def test_functions(self):
        """This function tests if BaseModel moudule is documented.
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_attributes(self):
        """This function test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.BaseModel1, 'name'))
        self.assertTrue(hasattr(self.BaseModel1, 'id'))
        self.assertTrue(hasattr(self.BaseModel1, 'created_at'))
        self.assertTrue(hasattr(self.BaseModel1, 'updated_at'))

    def test_set_attributes(self):
        """This function tests the  set attributes of BaseModel.
        """
        self.assertEqual(self.BaseModel1.name, "Nokia")
        self.assertEqual(self.BaseModel1.my_number, 33)

    def test_to_dict(self):
        """This function tests if to_dict method is working correctly.
        """
        my_model_json = self.BaseModel1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.BaseModel1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.BaseModel1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.BaseModel1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.BaseModel1.id)

    def test_unique_id(self):
        """This function tests if each instance is created with a unique ID.
        """
        basemodel2 = self.BaseModel1.__class__()
        basemodel3 = self.BaseModel1.__class__()
        basemodel4 = self.BaseModel1.__class__()
        self.assertNotEqual(self.BaseModel1.id, basemodel2.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel3.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel4.id)

    def test__str__(self):
        """This function tests if __str__ method returns expected string.
        """
        string = str(self.BaseModel1)
        id_test = "[BaseModel] ({})".format(self.BaseModel1.id)
        boolean = id_test in string
        self.assertEqual(True, boolean)
        boolean = "updated_at" in string
        self.assertEqual(True, boolean)
        boolean = "created_at" in string
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in string
        self.assertEqual(True, boolean)


if __name__ == '__main__':
    unittest.main()
