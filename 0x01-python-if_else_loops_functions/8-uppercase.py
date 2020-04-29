#!/usr/bin/python3
def uppercase(str):
    str_cpy = list(str)
    for s in range(len(str_cpy)):
        if ord(str_cpy[s]) > 96 and ord(str_cpy[s]) < 123:
            str_cpy[s] = chr(ord(str_cpy[s]) - 32)
        print("{:s}".format(str_cpy[s]), end="")
    print()
