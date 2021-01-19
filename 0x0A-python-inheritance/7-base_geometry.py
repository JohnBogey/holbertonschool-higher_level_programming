#!/usr/bin/python3
"""Creates a geometry class"""


class BaseGeometry:
    """class that defines a geometry"""
    def area(self):
        """returns area of object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
