#!/usr/bin/python3
""" This script defines a class TestFileStorage to test the FileStorage module. """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """This class blueprint defines tests for FileStorage Class"""

    @classmethod
    def setUp(cls):
        """This function runs for each test case.
        """
        cls.base_model1 = BaseModel()
        cls.file_storage1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """This function cleans up after each test.
        """
        del cls.base_model1
        del cls.file_storage1

    def test_class_exists(self):
        """This function tests if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.file_storage1)), result)

    def test_types(self):
        """This function tests if attributes type is correct.
        """
        self.assertIsInstance(self.file_storage1, FileStorage)
        self.assertEqual(type(self.file_storage1), FileStorage)

    def test_functions(self):
        """This function tests if FileStorage module is documented.
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """This function tests if save method is working correctly.
        """
        self.file_storage1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """This function tests if reload method is working correctly.
        """
        self.base_model1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
