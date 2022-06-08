#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for a in set_1:
        for b in set_2:
            if a == b:
                new_list.append(a)
    return new_list
