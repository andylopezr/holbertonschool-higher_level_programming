#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Returns the area of Square"""
        return self.__size ** 2
