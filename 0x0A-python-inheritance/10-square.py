#!/usr/bin/python3
"""Creates a square subclass"""


r = __import__('9-rectangle').Rectangle


class Square(r):
    """class that defines a square subclass"""

    def __init__(self, size):
        """inits vals"""
        r.__init__(self, size, size)
        self.__size = size
