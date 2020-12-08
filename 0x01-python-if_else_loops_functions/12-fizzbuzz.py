#!/usr/bin/python3
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz", end="")
    if n % 5 == 0:
        print("Buzz", end="")
    if n % 3 == 0 or n % 5 == 0:
        print(" ", end="")
    else:
        print("{:d} ".format(n), end="")
print()
