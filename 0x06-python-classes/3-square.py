#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Private instance attribute size of type int"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns area of the Square"""
            return self.__size * self.__size
