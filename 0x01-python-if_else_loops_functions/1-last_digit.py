#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d}".format(number), end=' ')
if number > 0 and number % 10 > 5:
    print("is {:d}".format(number % 10), end=' ')
    print("and is greater than 5")
elif number % 10 == 0:
    print("is {:d}".format(number % 10), end=' ')
    print("and is 0")
elif number < 0:
    print("is {:d}".format(number % -10), end=' ')
    print("and is less than 6 and not 0")
else:
    print("is {:d}".format(number % 10), end=' ')
    print("and is less than 6 and not 0")
