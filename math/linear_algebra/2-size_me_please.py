#!/usr/bin/env python3
"""
This module contains a function to calculate the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    # Handle edge case for empty matrix
    if not matrix:
        return []

    # Initialize the shape list
    shape = []

    # Iterate though each level to calculate shape
    while isinstance(matrix, list):  # The current matrix is a list
        shape.append(len(matrix))    # The lenght of the current level
        matrix = matrix[0]

    return shape
