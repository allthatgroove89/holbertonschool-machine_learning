#!/usr/bin/env python3
"""
This module provides a function to transpose a 2D matrix.
"""


import numpy as np


def np_transpose(matrix):
    """
    Transposes a matrix.

    Args:
        matrix (list of lists): A 2D matrix to transpose.

    Returns:
        list of lists: The transposed matrix.
    """
    return np.transpose(matrix)
