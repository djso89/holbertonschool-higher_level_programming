#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        cnt = 0
        for i in n:
            if len(n) - 1 > cnt:
                print("{:d}".format(i), end=' ')
            else:
                print("{:d}".format(i), end='')
            cnt += 1
        print()
