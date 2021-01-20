#!/usr/bin/python3
"""Defines a function that prints a UTF-8 text file"""


def read_file(filename=""):
    """Reads and prints a UTF-8 encoded file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
