#!/usr/bin/python3
"""Defines BaseGeometry class"""


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
