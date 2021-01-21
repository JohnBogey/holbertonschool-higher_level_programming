#!/usr/bin/python3
"""my vals"""


class MyInt(int):
    """my int"""

    def __init__(self, val):
        """inits vals"""
        self.__val = int(val)

    def __eq__(val, other):
        """eq vals"""
        return int.__ne__(val, other)

    def __ne__(val, other):
        """ne vals"""
        return int.__eq__(val, other)
