#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_string = roman_string.upper()
    value = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev = 0
    ans = 0
    n = len(roman_string)
    for i in range(n - 1, -1, -1):
        if value[roman_string[i]] >= prev:
            ans += value[roman_string[i]]
        else:
            ans -= value[roman_string[i]]
        prev = value[roman_string[i]]
    return ans
