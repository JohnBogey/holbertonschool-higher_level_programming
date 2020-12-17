#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for index, element in enumerate(matrix):
        new_matrix.append(list(map(lambda x: x ** 2, element)))
    return new_matrix
