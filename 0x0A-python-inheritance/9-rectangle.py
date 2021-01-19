#!/usr/bin/python3
"""Creates a rectangle subclass"""


bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """class that defines a rectangle subclass"""

    def __init__(self, width, height):
        """inits vals"""
        try:
            super().integer_validator("width", width)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        self.__width = width

        try:
            super().integer_validator("height", height)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        self.__height = height

    def area(self):
        """returns area of rect"""
        return self.__width * self.__height

    def __str__(self):
        """str method for rect subclass"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
