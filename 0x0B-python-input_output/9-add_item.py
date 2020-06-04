#!/usr/bin/python3
"""
script that adds all arguments to python list and
save them to file
"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

a = []

try:
    a = load_from_json_file("add_item.json")

except:
    pass

for i in sys.argv[1:]:
    a.append(i)

save_to_json_file(a, "add_item.json")
