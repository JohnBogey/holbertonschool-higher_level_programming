#!/usr/bin/python3
"""prints a square based on size, if valid"""


def print_square(size):
    """checks validity of size then runs"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
