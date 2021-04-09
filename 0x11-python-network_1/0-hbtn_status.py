#!/usr/bin/python3
""" Fetches a basic request using urllib"""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    r = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(r), r, r.decode('utf-8')))
