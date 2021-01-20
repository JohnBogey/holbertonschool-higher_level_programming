#!/usr/bin/python3
"""create obj from json"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except:
    with open(filename, mode="w"):
        items = []
items += argv[1:]
save_to_json_file(items, filename)
