#!/usr/bin/python3
"""Creates a rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        '''sets width, height'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle 0 if h or w is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
