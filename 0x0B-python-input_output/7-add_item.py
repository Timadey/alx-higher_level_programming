#!/usr/bin/python3
"""Add Items Modules
Attributes:
    arg, add_item_file
"""


from sys import argv

arg = argv[1:]
add_item_file = "add_item.json"

with open(add_item_file, mode="w", encoding="utf-8") as json_file:
    load_from_json_file = __import__("6-load_from_json_file.py")

    list_from_json = load_from_json_file(add_item_file)
    arg.extend(list_from_json)
    
    save_to_json_file = __import__("5-save_to_json_file.py")
    save_to_json_file(arg, add_item_file)
