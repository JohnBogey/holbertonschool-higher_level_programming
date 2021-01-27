#!/usr/bin/python3
"""square class, inherits rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a class named Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructs class"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """updates rectangle"""
        if (args and args != []):
            key = ["id", "size", "x", "y"]
            for i in range(0, len(args)):
                setattr(self, key[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns dict representation of square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """returns str"""
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """property to retrieve"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter"""
        self.validate_size(value, "width")
        self.width = value
        self.height = value
