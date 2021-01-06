#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        '''sets size and position'''
        self.size = size
        self.position = position

    @property
    def size(self):
        """property to retrieve"""
        return self.__size

    @size.setter
    def size(self, size):
        """property setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """property to retrieve"""
        return self.__position

    @position.setter
    def position(self, position):
        """property setter"""
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        '''returns area of square'''
        return self.__size ** 2

    def my_print(self):
        '''prints square'''
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
    
    def __str__(self):
        '''prints square, for usage with print()'''
        square_string = ""
        if self.__size == 0:
            return square_string
        else:
            for i in range(self.__position[1]):
                square_string += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    square_string += " "
                for j in range(self.__size):
                    square_string += "#"
                if i < self.__size - 1:
                    square_string += "\n"
        return square_string
