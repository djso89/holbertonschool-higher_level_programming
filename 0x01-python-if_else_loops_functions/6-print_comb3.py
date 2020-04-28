#!/usr/bin/python3
for n in range(1, 90):
    if n is 89:
        print("{:02d}".format(n))
        break
    if (n % 10) > (n / 10):
        print("{:02}".format(n), end=", ")
