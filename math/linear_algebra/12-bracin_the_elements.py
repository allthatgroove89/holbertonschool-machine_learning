#!/usr/bin/env python3
"""
This module provides a function to perform
element-wise operations on two matrices.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction,
    multiplication, and division.

    Args:
        mat1 (numpy.ndarray): First input matrix.
        mat2 (numpy.ndarray): Second input matrix.

    Returns:
        tuple: A tuple containing the element-wise sum,
        difference, product, and quotient.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
