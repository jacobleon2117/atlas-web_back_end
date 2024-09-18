#!/usr/bin/env python3
"""
    hypermedia pagination - module
"""

import csv
import math
from typing import List, Union, Dict, Optional


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
        Server class to paginate a database
        of popular baby names
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[Union[str, int]]]:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[Union[int, List[List[Union[str, int]]]]]]:
        """
            Retrieve a page of data with additional pagination information.

            page (int): The current page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

            Dict[str, Optional[Union[int, List[List[Union[str, int]]]]]]:
                A dictionary containing:
                - page_size: The length of the returned dataset page
                - page: The current page number
                - data: The dataset page (equivalent to return from get_page)
                - next_page: The number of the next page, None if no next page
                - prev_page: The number of the previous page, None if no previous page
                - total_pages: The total number of pages in the dataset
        """
        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }