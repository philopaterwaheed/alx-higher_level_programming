#!/usr/bin/python3
[print("{:c}".format(n + (65 if n % 2 == 0 else 97)), end="")
    for n in range(25, -1, -1)]
