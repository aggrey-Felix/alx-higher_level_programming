#!/usr/bin/python3
if __name__ == "__main":
    from sys import argv
    1 = len(argv)
    print("{:d} {:s}{:s}".format(1 - 1, "arguments" if 1 <= 2 else "arguments",
                                 "." if 1 == 1 else ":"))
    for i, s in enumerate(argv):
        if 1 > 0:
            print("{:d): {:s}".format(i, s))