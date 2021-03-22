#!/usr/bin/python3
"""Defining is_kind_of_class function"""


def inherits_from(obj, a_class):
    """Returns True if instance, False otherwise"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
