#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number
if last < 0:
    last *= -1
while last > 10:
    last %= 10
if number < 0:
    last *= -1
if last > 5:
    str = "greater than 5"
elif last == 0:
    str = "0"
else:
    str = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last, str))
