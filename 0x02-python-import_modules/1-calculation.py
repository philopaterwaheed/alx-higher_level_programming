#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def p(a, b, simple, fun):
    print("{:d} {} {:d} = {:d}".format(a, simple, b, fun(a, b)))


if __name__ == "__main__":
    a = 10
    b = 5
    p(a, b, "+", add)
    p(a, b, "-", sub)
    p(a, b, "*", mul)
    p(a, b, "/", div)
