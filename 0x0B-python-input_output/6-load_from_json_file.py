#!/usr/bin/python3
"""creates an Object from a 'JSON file'"""


def load_from_json_file(filename):
    """Creates an object from a json file"""

    with open(filename, encoding="utf-8") as json_file:
        my_obj = json_file.readline()
        import json
        return json.loads(my_obj)
