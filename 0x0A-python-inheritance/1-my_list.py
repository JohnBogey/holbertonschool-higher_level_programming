#!/usr/bin/python3
"""prints sorted list"""


class MyList(list):
    """inherits from class list"""

    def print_sorted(self):
        """method that prints sorted list"""
        print(sorted(self))
