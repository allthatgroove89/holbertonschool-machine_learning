#!/usr/bin/env python3
"""
A function that performs matrix multipliation.
"""


import numpy as np


def np_matmul(mat1, mat2):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
        mat1 (numpy.ndarray): First input matrix.
        mat2 (numpy.ndarray): Second input matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(mat1, mat2)
