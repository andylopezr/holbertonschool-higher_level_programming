#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Rectangle class initialization"""
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width attribute"""
        if type(value) is not int:
                raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Prints Rectangle with # Character"""
        if self.__width == 0 or self.__height == 0:
                return ""
        string = ""
        for i in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string

    def __repr__(self):
        """Returns the representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.width * 2 + self.height * 2
