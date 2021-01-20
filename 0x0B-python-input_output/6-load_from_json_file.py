#!/usr/bin/python3
"""create obj from json"""


import json


def load_from_json_file(filename):
    """function that creates obj from file"""
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
