#!/usr/bin/python3
"""Class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """Base class for geometry objects"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is int and greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry"""

    def __init__(self, width, height):
        """Rectangle Instantation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns info about Rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Returns the area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
