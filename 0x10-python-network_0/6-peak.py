#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ recursion method """
    numbers = list_of_integers

    if len(numbers) == 0 or numbers is None:
        return None

    if (len(numbers) == 1):
        return (numbers[0])

    if numbers[0] > numbers[1]:
        return (numbers[0])

    if numbers[-1] > numbers[-2]:
        return numbers[-1]

    mid = len(numbers) // 2

    if (numbers[mid - 1] > numbers[mid]):
        return (find_peak(numbers[:mid]))
    elif (numbers[mid - 1] > numbers[mid]):
        return (find_peak(numbers[mid + 1:]))
    else:
        return(numbers[mid])
