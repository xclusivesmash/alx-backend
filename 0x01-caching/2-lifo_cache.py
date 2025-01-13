#!/usr/bin/python3
"""
module: 2-lifo_cache
description: implements the LIFO algorithm to the
caching system defined.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
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
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            KEY, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(KEY))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Extracts items by key"""
        return self.cache_data.get(key, None)
