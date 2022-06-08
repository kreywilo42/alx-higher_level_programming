#!/usr/bin/python3
def no_c(my_string):
    second_string = my_string.translate({ord(a): None for a in 'cC'})
    return second_string
