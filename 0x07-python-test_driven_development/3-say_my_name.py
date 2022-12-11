#!/usr/bin/python3
"""Module to Print 'My name is '
"""


def say_my_name(first_name, last_name=""):
    """Function to Print 'My name is ' followed by first and last name
        @first_name: string first_name
        @last_name: string last_name
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")
    print("My name is {:s}".format(first_name + ' ' + last_name))
