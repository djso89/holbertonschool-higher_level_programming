#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a
    text file and returns the number of chars added
    """
    with open(filename, 'a') as f:
        chars = f.write(text)
    return chars
