#!/usr/bin/env python3
"""
    index_range - module
"""


def index_range(page, page_size):
    """
        Return a tuple of start and end index for pagination.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
