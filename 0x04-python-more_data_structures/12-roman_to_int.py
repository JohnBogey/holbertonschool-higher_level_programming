#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    r_to_i = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    for i, char in enumerate(roman_string):
        if i + 1 < len(roman_string):
            if r_to_i[char] < r_to_i[roman_string[i + 1]]:
                total -= r_to_i[char]
                continue
        total += r_to_i[char]
    return total
