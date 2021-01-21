#!/usr/bin/python3
"""adds attr if possible"""


def add_attribute(obj, name, val):
    """adds attr"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, val)
