#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a != ord('q') and a != ord('e'):
        print('{:c}'.format(a), end="")
