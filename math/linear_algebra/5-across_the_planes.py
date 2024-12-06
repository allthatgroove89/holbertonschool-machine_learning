#!/usr/bin/env python3
"""
This module contains a function to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists of int/float): The first 2D matrix.
        mat2 (list of lists of int/float): The second 2D matrix.

    Returns:
        list of lists of int/float: A new 2D matrix containing
        the element-wise sums of mat1 and mat2.
        If mat1 and mat2 are not the same shape, returns None.
    """
    if len(mat1) != len(mat2):
        return None

    new_matrix = []

    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

        new_row = []

        for j in range(len(mat1)):
            new_row.append(mat1[i][j] + mat2[i][j])

        new_matrix.append(new_row)

    return new_matrix
