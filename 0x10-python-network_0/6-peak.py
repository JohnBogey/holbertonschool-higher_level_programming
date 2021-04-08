#!/usr/bin/python3
""" function to find peak """
def find_peak(list_of_integers):
    if not list_of_integers or len(list_of_integers) < 1:
        return None
    hill = list_of_integers
    for i in range(len(hill)):
        if hill[i - 1] < hill[i] and hill[i + 1] < hill[i]:
            return hill[i]
    return hill[len(hill) - 1]
