#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    x = len(matrix[0])
    if x > 0:
        for i in range(n):
            for j in range(x):
                print(matrix[i][j], end=" ")
            print()
    else:
        print()
