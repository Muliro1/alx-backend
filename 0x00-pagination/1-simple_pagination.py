#!/usr/bin/env python3
""" module doc """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ func doc """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page from the dataset.

        Args:
            page (int): The page number. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: The page of the dataset.
        """
        # Assert that the page and page_size are integers and positive
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # Calculate the start and end indices of the page
        start, end = self.index_range(page, page_size)

        # Return the page of the dataset
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end indices of a page in the dataset.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: The start and end indices of the page.
        """
        # Calculate the start index of the page
        start_index = (page - 1) * page_size

        # Calculate the end index of the page
        end_index = page * page_size

        # Return the start and end indices of the page
        return (start_index, end_index)
