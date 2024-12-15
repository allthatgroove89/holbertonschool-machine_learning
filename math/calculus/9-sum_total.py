#!/usr/bin/env python3
"""
Module: sum_total
This module provides a function to calculate the sum of squares from 1 to n.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares from 1 to n using the formula:
    Sum = n(n + 1)(2n + 1) / 6

    Parameters:
    n (int): The stopping condition

    Returns:
    int: The integer value of the sum, or None if n is invalid
    """
    if not isinstance(n, int) or n < 1:
        return None  # Return None for invalid inputs

    # Apply the formula
    return (n * (n + 1) * (2 * n + 1)) // 6
