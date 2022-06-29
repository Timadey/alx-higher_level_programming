#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        d = ord(char)
        if d in range(97, 123):
            new_str += chr(d - 32)
        else:
            new_str += char
    print("{:s}".format(new_str))
