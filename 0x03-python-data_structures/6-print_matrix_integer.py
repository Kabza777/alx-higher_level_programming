#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(len(row)):
            print("{:d}".format(row[idx]), end="")
            if idx < len(row) - 1:
                print(" ", end="")
        print("")
