#!/usr/bin/python3
"""Defining is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if exact instance, False otherwise"""
    return type(obj) == a_class
