#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        msg = ""
        if n % 3 == 0:
            msg = msg + "Fizz"
        if n % 5 == 0:
            msg = msg + "Buzz"
        if not msg:
            msg = str(n)
        print(msg, end=" ")
