#!/usr/bin/python3
from sys import argv
from functools import reduce

if __name__ == "__main__":
    print(reduce(lambda a, b: int(a) + int(b), argv[1:], 0))
