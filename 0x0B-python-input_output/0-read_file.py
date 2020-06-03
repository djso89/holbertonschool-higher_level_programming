#!/usr/bin/python3
"""read_file module """


def read_file(filename=""):
    """
    read the file and print out to
    stdout
    """
    with open(filename) as f:
        content = f.read()
    print(content, end='')
