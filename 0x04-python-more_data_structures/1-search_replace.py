#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for a in range(len(my_list)):
        if my_list[a] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[a])
    return new_list
