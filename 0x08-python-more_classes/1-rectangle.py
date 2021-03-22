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
