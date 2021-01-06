#!/usr/bin/python3
"""comments
"""

import math


class MagicClass:
    """comment"""
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
    """comment"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
    """comment"""
        return self.__radius * math.pi * 2
