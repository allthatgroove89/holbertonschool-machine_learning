#!/usr/bin/env python3

def matrix_shape(matrix):
    # Handle edge case for empty matrix
    if not matrix:
        return []

    # Initialize the shape list
    shape = []

    # Iterate though each level to calculate shape
    while isinstance(matrix, list): # The current matrix is a list
        shape.append(len(matrix))   # The lenght of the current level
        matrix = matrix[0]

    return shape
