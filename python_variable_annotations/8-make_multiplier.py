#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.
"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a 
        float and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
