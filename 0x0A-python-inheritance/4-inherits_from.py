#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
