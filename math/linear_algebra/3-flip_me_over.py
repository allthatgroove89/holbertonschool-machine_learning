#!/usr/bin/env python3
"""
This module contains a function to calculate the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The original matrix.

    Returns:
        list of lists: The transposed matrix.
    """
    transposed = []

    for i in range(len(matrix[0])):
        new_row = [row[i] for row in matrix]
        transposed.append(new_row)

    return transposed
