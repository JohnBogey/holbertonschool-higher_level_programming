#!/usr/bin/python3
"""Prints a string, but adds newlines"""


def text_indentation(text):
    """prints string assuming text is valid"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    n = text.replace(".", ".\n\n").replace(":", ":\n\n").replace("?", "?\n\n")
    n = n.replace("\n ", "\n")
    print(n, end="")
