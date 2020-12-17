#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    winner = "nobody"
    best_score = 0
    for key, value in a_dictionary.items():
        if value > best_score:
            winner = key
    return winner
