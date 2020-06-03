#!/usr/bin/python3
def number_of_lines(filename=""):
    line_num = 0
    with open(filename) as f:
        for line in f:
            line_num += 1
    return line_num
