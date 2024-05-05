#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns a dictionary of the dataset, indexed by the sorting position,
        starting at 0.

        This method is used to create a deletion-resilient dataset.
        """
        if self.__indexed_dataset is None:
            # Load the dataset
            dataset = self.dataset()

            # Truncate the dataset to the first 1000 entries
            truncated_dataset = dataset[:1000]

            # Create an indexed dataset
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a hypermedia index for a given position and page size.

        Args:
            index (int): The index of the dataset to start from.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing the index, next index, page size,
                  and data.
        """
        # Assert that the index and page_size are integers and positive
        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        assert 0 <= index < len(self.__indexed_dataset)

        # Initialize the next index as the current index
        next_index = index

        # Initialize an empty list to store the data
        data = []

        # Loop through the indices of the page
        for i in range(index, index + page_size):
            # If the index is in the dataset,
            # append the data and update the next index
            if i in self.__indexed_dataset:
                data.append(self.__indexed_dataset[i])
                next_index = i

        # Return the hypermedia index as a dictionary
        return {
            "index": index,
            "next_index": next_index + 1,
            "page_size": page_size,
            "data": data,
        }
