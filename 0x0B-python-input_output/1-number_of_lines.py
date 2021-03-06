#!/usr/bin/python3
""" number of lines module """


def number_of_lines(filename=""):
    """
    function that returns
    the number of lines of a text file
    """
    line_num = 0
    with open(filename) as f:
        for line in f:
            line_num += 1
    return line_num
