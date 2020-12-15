#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for pos in row:
            if i is not 0:
                print(" ", end = "")   
            else:
                i += 1
            print("{:d}".format(pos), end = "")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
