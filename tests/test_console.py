#!/usr/bin/python3
"""This python script defines a class TestHBNBCommandDocs 
for HBNBCommand class/ console"""

import unittest
import console
from console import HBNBCommand
import pep8

class TestHBNBCommandDocs(unittest.TestCase):
    """Test case for HBNBCommand documentation
    """

    def test_console_conforms_pep8(self):
        """Test case to ensure that console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testconsole_conforms_pep8(self):
        """Test case that ensures tests/test_console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Test case for the module docstring.
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstr(self):
        """Test case for HBNBCommand class docstring.
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
