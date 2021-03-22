#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Private instance attribute size of type int"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
