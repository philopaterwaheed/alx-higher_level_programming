#!/usr/bin/env python3
def no_c(my_string):
    rt = ""
    for c in my_string:
        if c != "c" and c != "C":
            rt = rt + c
    return (rt)
