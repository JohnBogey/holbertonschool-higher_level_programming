#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """function that writes a file"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
