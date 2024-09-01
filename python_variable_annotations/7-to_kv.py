#!/usr/bin/env python3

"""
This module provides a function to create a tuple containing a string and the square of a number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string and the second element is the square of a number.

    Args:
        k (str): A string to be the first element of the tuple.
        v (Union[int, float]): An integer or float to be squared and used as the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k and the second element is the square of v.
    """
    return (k, float(v ** 2))
