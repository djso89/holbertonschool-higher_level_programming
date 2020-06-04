#!/usr/bin/python3
"""load_from_json_file module """


def load_from_json_file(filename):
    """
    a function that creates an Object from a JSON file
    """
    import json
    with open(filename, "r") as jf:
        return json.load(jf)
