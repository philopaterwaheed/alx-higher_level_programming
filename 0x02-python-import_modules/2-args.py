#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    print("{:d} argument{}{}".format(
        count, "" if count == 1 else "s", "." if not count else ":"))
    for i, arg in enumerate(argv[1:]):
        print("{:d}: {}".format(i + 1, arg))
