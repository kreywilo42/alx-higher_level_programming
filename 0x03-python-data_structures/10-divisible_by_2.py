#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for a in my_list:
        if a % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
