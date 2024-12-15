#!/usr/bin/env python3
"""
Module: sum_total
This module provides a function to calculate the sum of squares from 1 to n.
"""


def summation_i_squared(n):
    """This function calculates the sum of the squares"""
    # Step 1: Validate the input
    if not isinstance(n, int) or n <= 0:
        return None  # Return None if n is not a valid number

    # Step 2: Apply the formula to calculate the sum of squares
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6

    # Step 3: Return the result
    return sum_squares
