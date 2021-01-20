#!/usr/bin/python3
"""Creates a student class"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """inits vals"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representation of student"""
        if type(attrs) is list:
            filtered = {}
            for elem in attrs:
                if type(elem) is str:
                    try:
                        filtered[elem] = self.__dict__[elem]
                    except:
                        pass
            return filtered
        return vars(self)

    def reload_from_json(self, json):
        """replaces all attributes of student instance"""
        for elem in json:
            self.__dict__[elem] = json[elem]
