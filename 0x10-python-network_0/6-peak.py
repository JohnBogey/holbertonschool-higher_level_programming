#!/usr/bin/python3
""" function to find peak """


def find_peak_recur(hill, low, high, length):
    """ recursive function to find a peak """
    mid = low + (high - low) / 2
    mid = int(mid)
    print("l[{}] c[{}] r[{}]".format(hill[mid - 1], hill[mid], hill[mid + 1]))
    if ((mid == 0 or hill[mid - 1] <= hill[mid]) and
       (mid == length - 1 or hill[mid + 1] <= hill[mid])):
        return hill[mid]
    elif (mid < length and hill[mid + 1] < hill[mid]):
        return find_peak_recur(hill, low, (mid - 1), length)
    else:
        return find_peak_recur(hill, (mid + 1), high, length)


def find_peak(list_of_integers):
    """ wrapper function to run recur func """
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    return find_peak_recur(list_of_integers, 0, length - 1, length)
