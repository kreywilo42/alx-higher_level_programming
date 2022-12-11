#!/usr/bin/python3
"""Module to Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divides all elements of a matrix
        @matrix:  list of lists of ints or floats
        @div: int or float
        Return: new matrix
    """
    mat_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(mat_err)
    temp = []
    new_m = []
    list_len = len(matrix[0])
    for i_list in matrix:
        for i in i_list:
            if isinstance(i, float) is not True:
                if isinstance(i, int) is not True:
                    raise TypeError(mat_err)
            if isinstance(div, float) is not True:
                if isinstance(div, int) is not True:
                    raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            temp.append(round(i / div, 2))
        if list_len != len(temp):
            raise TypeError("Each row of the matrix must have the same size")
        new_m += [temp]
        temp = []
    return new_m
