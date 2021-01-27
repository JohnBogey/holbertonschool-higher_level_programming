#!/usr/bin/python3
"""Unittest for almost a circle files, classes, and methods
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInit(unittest.TestCase):
    """Testing init for base class"""

    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_base_init(self):
        """adding simple instances"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_str(self):
        """test to json_str"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        reverted = Base.from_json_string(json_dictionary)
        expected = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertDictEqual(reverted, expected)

    def test_save_to_file(self):
        """test save to file"""
        pass

    def test_create(self):
        """test create"""
        pass

    def test_load_from_file(self):
        """test load from file"""
        pass
