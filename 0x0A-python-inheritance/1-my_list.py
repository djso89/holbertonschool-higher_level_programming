#!/usr/bin/python3
"""Inherited list class MyList"""


class MyList(list):
    """
    list
    """
    def print_sorted(self):
        """
        Sorts the list and prints the list
        """
        print(sorted(self))
