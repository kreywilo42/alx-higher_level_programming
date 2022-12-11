#!/usr/bin/python3
def update_dictionary(a_dic, key, val):
    if key not in a_dic:
        a_dic[key] = val
    else:
        for i in a_dic:
            if i == key:
                a_dic[i] = val
    return a_dic
