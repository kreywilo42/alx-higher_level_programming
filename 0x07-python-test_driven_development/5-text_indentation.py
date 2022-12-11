#!/usr/bin/python3
"""Module that prints text with two lines after '.', '?', ':'
"""


def text_indentation(text):
    """Function that prints text with two lines after '.', '?', ':'
        @text: text string
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    n_str = text.split()
    n_str = " ".join(n_str)
    n_str = n_str.replace(".", ".\n\n")
    n_str = n_str.replace(":", ":\n\n")
    n_str = n_str.replace("?", "?\n\n")
    n_str = n_str.replace("\n ", "\n")
    #    if i == ',' or i == ':' or i == '?':
    print(n_str, end='')
