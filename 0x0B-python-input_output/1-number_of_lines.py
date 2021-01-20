#!/usr/bin/python3
"""Defines a function that line number in a UTF8 text file"""


def number_of_lines(filename=""):
    """Reads the file and returns number of lines"""
    with open(filename, "r") as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
