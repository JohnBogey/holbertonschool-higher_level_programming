#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """function that reads a file"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end='')
