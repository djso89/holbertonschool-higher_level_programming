#!/usr/bin/python3
"""write_file module """


def write_file(filename="", text=""):
    """
    function that writes string to a text
    file and returns the number of characters
    written
    """
    with open(filename, 'w') as f:
        chars = f.write(text)
    return chars
