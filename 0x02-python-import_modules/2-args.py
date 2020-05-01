#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    ac = len(sys.argv)
    if ac == 2:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    elif ac > 2:
        print("{:d} arguments:".format(ac - 1))
        for i in range(ac - 1):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
    else:
        print("0 arguments.")
