#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """check if object is instance of class
    that inherited from the specified class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
