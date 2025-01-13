#!/usr/bin/python3
"""
module: 1-fifo_cache
description: implements the FIFO algorithm to the
caching system defined.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ @description
    Attributes:
    Methods:
    """
    def __init__(self):
        """Initialize method."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item to cache system"""
        if key is None or item is None:
            return
        # limit check
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Extracts items by key"""
        return self.cache_data.get(key, None)
