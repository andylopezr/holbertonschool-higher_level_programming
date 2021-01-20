#!/usr/bin/python3
"""Makes a list from args and saves them to a file in JSON format"""
import sys
import json
savejson = __import__("5-save_to_json_file").save_to_json_file
loadjson = __import__("6-load_from_json_file").load_from_json_file

try:
    listy = loadjson("add_item.json")
except FileNotFoundError:
    listy = []
for arg in sys.argv[1:]:
    listy.append(arg)
savejson(listy, "add_item.json")
