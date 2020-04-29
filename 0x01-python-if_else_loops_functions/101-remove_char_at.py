#!/usr/bin/python3
def remove_char_at(str, n):
    s = str
    for i in range(len(s)):
        if i == n:
            s = s[0: i:] + str[i + 1::]
    return s
