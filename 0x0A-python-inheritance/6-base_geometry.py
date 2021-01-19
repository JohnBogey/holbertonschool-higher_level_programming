#!/usr/bin/python3
"""Creates a geometry class"""


class BaseGeometry:
    """class that defines a geometry"""
    def area(self):
        """returns area of object"""
        raise Exception("area() is not implemented")
