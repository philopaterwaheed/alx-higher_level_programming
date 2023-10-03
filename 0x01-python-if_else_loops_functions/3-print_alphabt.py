#!/usr/bin/python3
[print("{:c}".format(c), end="")
    for c in range(97, 123) if chr(c) not in ['e', 'q']]
