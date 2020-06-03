#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    """
    if obj:
        return dir(obj)
    else:
        pass
