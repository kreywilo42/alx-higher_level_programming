#!/usr/bin/python3
def square_matrix_simple(ma=[]):
    newmat = [[x ** 2 for x in row] for row in ma]
    return newmat
