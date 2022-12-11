#!/usr/bin/python3
def uniq_add(ml=[]):
    rs = 0
    ml = list(set(ml) | set(ml))
    for i in ml:
        rs += i
    return rs
