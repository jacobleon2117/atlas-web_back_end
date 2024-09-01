#!/usr/bin/env python3

"""
This module provides a function to calculate the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the elements in the list, represented as a float.
    """
    return float(sum(input_list))
