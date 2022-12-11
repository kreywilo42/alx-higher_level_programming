#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    for i in sorted(a_dic):
        print("{:s}: {}".format(i, a_dic[i]))
