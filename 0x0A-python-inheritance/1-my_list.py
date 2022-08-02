#!/usr/bin/python3
"""Inheritance"""


class MyList(list):
    """a class that inherits from `list`"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        new_list = [i for i in sorted(self)]
        print(new_list)
