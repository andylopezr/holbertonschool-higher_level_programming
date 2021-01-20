#!/usr/bin/python3
"""Defines a function that loads an object from a file's JSON string"""
import json


def load_from_json_file(filename=""):
    """Loaads an object from a file's JSON string"""
    with open(filename, "r") as f:
        return json.load(f)
