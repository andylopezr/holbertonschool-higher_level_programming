#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """subclass of list"""

    def print_sorted(self):
        """Prints MyList, sorted"""
        print(sorted(self))
