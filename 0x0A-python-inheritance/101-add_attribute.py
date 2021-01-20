#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    """Safely adds atributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
