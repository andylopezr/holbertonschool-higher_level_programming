#!/usr/bin/python3
"""Displays the value of Id from the header using URL as arg"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
