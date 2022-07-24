#!/usr/bin/python3
"""Print name give the fist and last name"""

def say_my_name(first_name, last_name=""):
    """Prints a name
    Args:
        first_name: the first name
        last_name: the last name
    
    Return:
        prints the name
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
