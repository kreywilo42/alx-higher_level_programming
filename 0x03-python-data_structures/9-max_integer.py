#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        highest_number = my_list[0]
        for a in my_list:
            if a > highest_number:
                highest_number = a

        return highest_number
