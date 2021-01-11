#!/usr/bin/python3
"""Creates a rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        '''sets width, height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve"""
        return width.__width

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
        return height.__height

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
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        '''returns string for usage with print()'''
        rect_string = ""
        if self.__width == 0 or self.__height == 0:
            return rect_string
        for i in range(self.__height):
            rect_string += "#" * self.__width
            if i < self.__height - 1:
                rect_string += "\n"
        return rect_string
