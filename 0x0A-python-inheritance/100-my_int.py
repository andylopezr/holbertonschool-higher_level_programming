#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Integer but with operators == and != inverted"""

    def __init__(self, myint):
        self.myint = myint

    def __eq__(int1, int2):
        """"replaces != for =="""
        return int1.myint != int2

    def __ne__(int1, int2):
        """replaces == for !="""
        return int1.myint == int2
