#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d}".format(number), end=' ')
ld = abs(number) % 10
if number < 0:
    ld = -ld
if ld > 5:
    print("is {:d}".format(ld), end=' ')
    print("and is greater than 5")
elif ld == 0:
    print("is {:d}".format(ld), end=' ')
    print("and is 0")
else:
    print("is {:d}".format(ld), end=' ')
    print("and is less than 6 and not 0")
