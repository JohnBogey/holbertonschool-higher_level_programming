#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for pos in row:
            if i is not 0:
                print(" ", end="")
            else:
                i += 1
            print("{:d}".format(pos), end="")
        print()
