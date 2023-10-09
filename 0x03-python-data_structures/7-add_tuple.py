#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    alen = len(tuple_a if tuple_a is not None else ())
    blen = len(tuple_b if tuple_a is not None else ())
    a = (tuple_a[0] if alen >= 1 else 0) + (tuple_b[0] if blen >= 1 else 0)
    b = (tuple_a[1] if alen >= 2 else 0) + (tuple_b[1] if blen >= 2 else 0)
    return (a, b)
