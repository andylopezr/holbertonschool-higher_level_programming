#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""
    def area(self):
        raise Exception("area() is not implemented")
