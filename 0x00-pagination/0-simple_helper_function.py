#!/usr/bin/env python3
"""
module: 0-simple_helper_function
description: returns a tuple of size two containing
a start index and an end index corresponding to the
range of indexes to return in a list for those particular
pagination parameters as specified in the function args.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """retrives an index range from the given args."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
