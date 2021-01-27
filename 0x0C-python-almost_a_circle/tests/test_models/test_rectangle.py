#!/usr/bin/python3
"""Unittest for almost a circle files, classes, and methods
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """testing for rectangle class"""

    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_init(self):
        """adding simple rect instances"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_validate(self):
        """tests the validator"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """tests area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_0(self):
        """tests simple display"""
        expected = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6)
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str_overwrite(self):
        """tests __str__ method"""
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(5, 5, 1)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_1(self):
        """tests simple display"""
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)
        expected = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(3, 2, 1, 0)
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_update_0(self):
        """tests update"""
        expected = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 2, 3, 4, 5)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_update_1(self):
        """tests update"""
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (89) 3/1 - 2/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(y=1, width=2, x=3, id=89)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(x=1, height=2, y=3, width=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_to_dict(self):
        """tests to dict"""
        self.maxDiff = None

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dictionary, expected)

        expected = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(r1_dictionary))
            self.assertEqual(fake_out.getvalue(), expected)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r2.to_dictionary(), expected)
