#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes to a file @filename
    Arguments:
        filename: the name of the file to write to
        text: the text to write in the file specified
    """

    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
