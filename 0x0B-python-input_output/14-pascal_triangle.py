#!/usr/bin/python3
"""pascal_triangle module """


def pascal_triangle(n):
    """
    function that returns a list of integers
    representing the Pascal's triangle of n
    """
    pt_list = []

    if n <= 0:
        return pt_list
    else:
        for i in range(n):
            new_list = []
            new_list.append(1)
            if len(pt_list) > 1:
                for k in range(len(pt_list[(len(pt_list) -1)])):
                    if k < (len(pt_list[(len(pt_list) - 1)]) - 1):
                        new_list.append(pt_list[len(pt_list) - 1][k] +
                                        pt_list[len(pt_list) - 1][k + 1])
            if len(pt_list) > 0:
                new_list.append(1)
            pt_list.append(list(new_list))
        return pt_list
