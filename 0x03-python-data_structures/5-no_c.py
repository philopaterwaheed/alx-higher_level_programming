#!/usr/bin/python3
def no_c(text):
    new = []
    for c in text:
        if c not in ['c', 'C']:
            new.append(c)
    return "".join(new)
