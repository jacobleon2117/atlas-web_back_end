#!/usr/bin/env python3

from typing import List, Tuple


"""
Module-level docstring: This module contains utility functions 
for working with lists of strings.
"""

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Computes the length of each string in a list of strings.

    Args:
        lst (List[str]): A list of strings for which the lengths 
        are to be computed.

    Returns:
        List[Tuple[str, int]]: A list of tuples 
        where each tuple contains a string and its length.
    
    Example:
        >>> element_length(["apple", "banana", "cherry"])
        [('apple', 5), ('banana', 6), ('cherry', 6)]
    """
    return [(i, len(i)) for i in lst]
