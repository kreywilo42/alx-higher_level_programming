#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for a in range(0, len(names)):
        if names[a][0:2] != "__":
            print("{}".format(names[a]))
