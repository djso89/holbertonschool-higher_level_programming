#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = dict(a_dictionary)
    for key in a_dict:
        a_dict[key] = a_dict[key] * 2
    return a_dict
