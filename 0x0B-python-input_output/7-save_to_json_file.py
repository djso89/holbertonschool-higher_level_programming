#!/usr/bin/python3
"""save_to_json_file module """


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a
    text file, using JSON representation
    """
    import json
    with open(filename, 'w+', encoding='utf-8') as jf:
        jf.write(json.dumps(my_obj))
