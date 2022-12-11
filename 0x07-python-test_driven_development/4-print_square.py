#!/usr/bin/python3
"""Module to prints a square
"""


def print_square(size):
    """Function to print a square with the '#' character
        @size: size of the square
    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
