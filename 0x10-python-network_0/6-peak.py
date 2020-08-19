#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_int):
    """ recursion method """
    numbers = list_int

    if len(numbers) == 0 or numbers is None:
        return None

    if (len(numbers) == 1):
        return (nums[0])

    if nums[0] > nums[1]:
        return (nums[0])

    if nums[-1] > nums[-2]:
        return numbs[-1]

    mid = len(numbers) // 2

    if (numbers[mid - 1] > numbers[mid]):
        return (find_peak(nums[:mid]))
    elif (numbers[mid - 1] > numbers[mid]):
        return (find_peak(nums[mid + 1:]))
    else:
        return(numbers[mid])
