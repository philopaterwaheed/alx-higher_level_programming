#!/usr/bin/python3
def uppercase(str):
    for n in str:
        n = ord(n)
        n = n - 32 if n >= 97 and n <= 122 else n
        print("{:c}".format(n), end="")
    print()
