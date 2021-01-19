#!/usr/bin/python3
"""checks if instance is subclass"""


def inherits_from(obj, a_class):
    """return true if obj is of subclass"""
    if type(obj) is a_class:
        return False
    return(issubclass(type(obj), a_class))
