#!/usr/bin/python3
"""Implements a Rectangle class from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
