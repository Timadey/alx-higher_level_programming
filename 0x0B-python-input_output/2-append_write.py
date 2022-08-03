#!/usr/bin/python3
"""Appends to a file"""


def append_write(filename="", text=""):
    """appends to a file @filename
    Arguments:
        filename: the name of the file to write to
        text: the text to write in the file specified
    """

    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
