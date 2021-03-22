#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Private instance attribute size of type int"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the Square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            string = '#' * self.__size
            for i in range(self.__size):
                print(string)
