#!/usr/bin/env python3
"""
    simple_pagination - module
"""

import csv
from typing import List, Union


def index_range(page: int, page_size: int) -> tuple:
    """
        Return a tuple of start and end index for pagination.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """
        Server class to paginate a
        database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[Union[str, int]]]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Retrieve a page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
