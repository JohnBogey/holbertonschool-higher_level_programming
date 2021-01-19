#!/usr/bin/python3
class MyInt(int):

    def __init__(self, val):
        """inits vals"""
        self.__val = int(val)

    def __eq__(val, other):
        int.__ne__(val, other)

    def __ne__(val, other):
        int.__eq__(val, other)
