#!/usr/bin/python3
""" Module to get the sum of two numbers
"""


def add_integer(a, b):
    """Function to sum two numbers
        @a: int or float
        @b: int or float
    """
    if isinstance(a, float) is not True and isinstance(a, int) is not True:
        raise TypeError("a must be an integer")
    if isinstance(b, float) is not True and isinstance(b, int) is not True:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
