#!/usr/bin/python3
"""add integer module """


def add_integer(a, b=98):
    if (type(a) == int or type(a) == float):
        if type(b) == int or type(b) == float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    elif not(isinstance(a, int) or isinstance(a, float)) and a is None:
        raise TypeError("a must be an integer")
