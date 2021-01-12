#!/usr/bin/python3
"""Module class with locked down attributes"""


class LockedClass:
    """Class with locked down attributes. Can only add first_name"""
    __slots__ = ['first_name']
