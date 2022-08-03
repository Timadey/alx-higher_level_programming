#!/usr/bin/python3
"""Read a text file"""


def read_file(filename=""):
    """Read a text file @filename"""

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
