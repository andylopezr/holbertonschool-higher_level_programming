#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    """Safely adds atributes"""
    try:
        setattr(obj, name, value)
    except:
        raise TypeError("can't add new attribute")
