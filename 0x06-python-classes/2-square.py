#!/usr/bin/python3
"""Creates a square class with size and checks for errors"""
class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        '''sets size and checks for errors'''
        if type(size) is not int:
            raise TypeError("size must be integer") 
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size =  size
