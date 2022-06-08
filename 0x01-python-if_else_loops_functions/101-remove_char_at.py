#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    a = 0
    for b in str:
        if a != n:
            new_str += str[a]
        a += 1
    return new_str
