#!/usr/bin/env python3
""" module doc """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start and end indices of the page.
    """
    # Calculate the starting index of the page
    startPage = (page - 1) * page_size

    # Calculate the ending index of the page
    endPage = page * page_size

    # Return the calculated indices as a tuple
    return (startPage, endPage)
