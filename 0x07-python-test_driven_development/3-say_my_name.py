#!/usr/bin/python3
"""say_my_name module """


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is
    <first_name> <last_name>
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    else:
        if isinstance(last_name, str) is False:
            raise TypeError("last_name must be a string")
        else:
            print("My name is {} {}".format(first_name, last_name))
