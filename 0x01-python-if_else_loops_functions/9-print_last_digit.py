#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    digit = 10 - digit if digit and number < 0 else digit
    print(digit, end="")
    return digit
