#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a 
list containing integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of the elements in the list, represented as a float.
    """
    return float(sum(mxd_lst))
