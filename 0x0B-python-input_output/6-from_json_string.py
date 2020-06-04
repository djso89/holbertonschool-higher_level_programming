#!/usr/bin/python3
"""from_json_string module """


def from_json_string(my_str):
    """
    function that returns an object
    represented by a JSON string
    """
    import json
    return json.loads(my_str)
