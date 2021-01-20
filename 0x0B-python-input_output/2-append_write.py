#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """function that appends a file"""
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
