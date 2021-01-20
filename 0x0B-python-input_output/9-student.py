#!/usr/bin/python3
"""Creates a student class"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """inits vals"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict representation of student"""
        return vars(self)
