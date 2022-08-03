#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    import json
    my_obj_json = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as json_file:
        json_file.write(my_obj_json)
