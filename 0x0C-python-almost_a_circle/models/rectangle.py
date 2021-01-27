#!/usr/bin/python3
"""rectangle class, inherits base"""


from models.base import Base


class Rectangle(Base):
    """a class named Rectangle that inherits from"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs class"""
        super().__init__(id)
        self.validate_size(width, "width")
        self.__width = width
        self.validate_size(height, "height")
        self.__height = height
        self.validate_pos(x, "x")
        self.__x = x
        self.validate_pos(y, "y")
        self.__y = y

    def update(self, *args, **kwargs):
        """updates rectangle"""
        if (args and args != []):
            key = ["id", "width", "height", "x", "y"]
            for i in range(0, len(args)):
                setattr(self, key[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def validate_size(self, value, name):
        """validates value for size"""
        if type(value) is not int:
            raise TypeError("{} must be an integer.".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0.".format(name))

    def validate_pos(self, value, name):
        """validates value for pos"""
        if type(value) is not int:
            raise TypeError("{} must be an integer.".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0.".format(name))

    @property
    def width(self):
        """property to retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter"""
        self.validate_size(value, "width")
        self.__width = value

    @property
    def height(self):
        """property to retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter"""
        self.validate_size(value, "height")
        self.__height = value

    @property
    def x(self):
        """property to retrieve"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""
        self.validate_pos(value, "x")
        self.__x = value

    @property
    def y(self):
        """property to retrieve"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""
        self.validate_pos(value, "y")
        self.__y = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle"""
        for i in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def to_dictionary(self):
        """returns dict representation of rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}

    def __str__(self):
        """returns str"""
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height))
