#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) > 96 and ord(s) < 123:
            print("{:c}".format(ord(s) - 32), end="")
        else:
            print("{:c}".format(ord(s)), end="")
    print()
