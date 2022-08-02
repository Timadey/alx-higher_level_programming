#!/usr/bin/python3
"""Module that houses the rebel MyInt"""


class MyInt(int):
    """The rebel that goes against the int"""

    def __eq__(self, otherInt):
        """Invert the equal to operator"""

        return int.__ne__(self, otherInt)

    def __ne__(self, otherInt):
        """Inverts the not equal to operator"""

        return int.__eq__(self, otherInt)
