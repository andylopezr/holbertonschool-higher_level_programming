#!/usr/bin/python3
"""Takes username and password to display id from Github"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(url, auth=auth)
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
