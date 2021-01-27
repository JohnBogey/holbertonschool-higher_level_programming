#!/usr/bin/python3
"""Unittest for almost a circle files, classes, and methods
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleInit(unittest.TestCase):
    """testing for square class"""

    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_square_init(self):
        """tests square init"""
        expected = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "25\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1.area())
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected)

        expected = "[Square] (2) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2 = Square(3, 1, 3)
            print(s2)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_square_get_set(self):
        """tests getter and setter of square"""
        expected = "[Square] (1) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            s1.size = 10
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_square_set_error(self):
        """tests error if bad size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(5)
            s1.size = "9"

    def test_square_update(self):
        """tests update of square"""
        expected = "[Square] (89) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            s1.size = 10
            s1.update(size=7, id=89, y=1, x=12)
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_square_to_dict(self):
        """tests square to dict"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1_dictionary, expected)
