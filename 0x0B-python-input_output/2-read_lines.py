#!/usr/bin/python3
"""read_lines module """


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file
    and prints it to stdout"""
    f = open(filename)
    cnt = len(f.readlines())
    with open(filename) as contents:
        if nb_lines <= 0 or nb_lines > cnt:
            words = contents.read()
            print(words, end='')
        else:
            for line in range(nb_lines):
                line = contents.readline()
                print(line, end='')
