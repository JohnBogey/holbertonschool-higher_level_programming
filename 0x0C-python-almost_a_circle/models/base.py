#!/usr/bin/python3
"""the first class, base"""


import json


class Base:
    """a class named base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructs class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that JSON to str"""
        if list_dictionaries is None:
            return("[]")
        return(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """function that JSON to str"""
        if json_string is None or json_string is "":
            return([])
        return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """function that saves to json file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        if (cls.__name__ == "Square"):
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """function that creates obj from file"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, encoding="utf-8") as a_file:
                return cls.create(cls.from_json_string(a_file))
        except:
            return []
