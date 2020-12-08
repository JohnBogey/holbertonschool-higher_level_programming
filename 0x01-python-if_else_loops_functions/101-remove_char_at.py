#!/usr/bin/python3
def remove_char_at(str, n):
    strNew = ""
    i = 0
    for x in str:
        if (i != n):
            strNew += x
        i += 1
    return strNew

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
