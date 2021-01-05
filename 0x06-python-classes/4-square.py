#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        '''sets size'''
        self.size = size

    @property
    def size(self):
        """property to retrieve"""
        return self.__size

    @size.setter
    def size(self, size):
        """property setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''returns area of square'''
        return self.__size ** 2
