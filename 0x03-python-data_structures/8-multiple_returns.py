#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
        l_f = length, first
        return l_f
    else:
        return 0, "None"
