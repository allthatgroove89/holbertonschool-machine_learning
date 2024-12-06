#!/usr/bin/env python3
"""
This module contains a function to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list of int/float): The first array.
        arr2 (list of int/float): The second array.

    Returns:
        list of int/float: A new list containing the
        element-wise sums of arr1 and arr2.
        If arr1 and arr2 are not the same length, returns None.
    """
    if len(arr1) != len(arr2):
        return None

    new_list = []

    for i in range(len(arr1)):
        new_list.append(arr1[i] + arr2[i])

    return new_list
