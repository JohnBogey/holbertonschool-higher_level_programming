#!/usr/bin/python3
"""adds integers"""


def add_integer(a, b=98):
    """adds and b, if b has no input then a + 98"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
