#!/usr/bin/env python3
"""
This module contains a function to multiply two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two 2D matrices.

    Args:
        mat1 (list of lists): The first 2D matrix.
        mat2 (list of lists): The second 2D matrix.

    Returns:
        list of lists: The resulting matrix after
        multiplication, or None if invalid dimensions.
    """
    # Check if the number of columns in mat1
    # is equal to the number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
