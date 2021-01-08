#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class holding tests for max integer function"""
    def test_poo(self):
        """Tests weird input"""
        self.assertEqual(max_integer(["poo", "poo"]), "poo")
    def test_integer(self):
        """Tests normal input"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    def test_empty(self):
        """Tests empty input"""
        self.assertEqual(max_integer([]), None)
    def test_string(self):
        """Tests string"""
        self.assertEqual(max_integer("ooh banana"), "o")
