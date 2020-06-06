#!/usr/bin/python3
"""add integer module """


def add_integer(a, b=98):
    """
    function that adds a and b
    """
    if (type(a) == int or type(a) == float):
        if type(b) == int or type(b) == float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
