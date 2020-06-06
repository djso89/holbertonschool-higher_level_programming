#!/usr/bin/python3
""" matrix_divided module """


def matrix_divided(matrix, div):
    """
    function that divides all elements of a
    matrix
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if isinstance(num, (int, float)) is False:
                raise TypeError(err)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not(type(div) == int or type(div) == float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2)for num in row] for row in matrix]
