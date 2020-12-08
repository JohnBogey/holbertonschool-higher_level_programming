#!/usr/bin/python3
def print_last_digit(number):
    last = number
    if last < 0:
        last *= -1
    while last > 10:
        last %= 10
    print(last, end="")
    return last
