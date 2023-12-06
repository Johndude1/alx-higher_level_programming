#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for numb in line:
            print("{:d}".format(numb), end = " ")
            print()
