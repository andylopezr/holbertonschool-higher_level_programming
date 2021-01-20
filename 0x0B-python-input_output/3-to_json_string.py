#!/usr/bin/python3
"""Defines a function that converts an object to a JSON string"""
import json


def to_json_string(my_obj):
    """Converts the object"""
    return json.dumps(my_obj)
