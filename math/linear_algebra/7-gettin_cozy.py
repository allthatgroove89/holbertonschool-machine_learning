#!/usr/bin/env python3
"""
This module contains a function to concatenate
two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.

    Args:
        mat1 (list of lists of int/float): The first 2D matrix.
        mat2 (list of lists of int/float): The second 2D matrix.
        axis (int): The axis along which
        to concatenate (0 for rows, 1 for columns).

    Returns:
        list of lists of int/float: A new 2D matrix
        containing the concatenated result.
        If the matrices cannot be concatenated, returns None.
    """
    if axis == 0:
        # Check if the number of columns in both matrices are the same
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Concatenate mat2 to the bottom of mat1
        return mat1 + mat2
    elif axis == 1:
        # Check if the number of rows in both matrices are the same
        if len(mat1) != len(mat2):
            return None
        # Concatenate mat2 to the right of mat1
        return [row1+row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
