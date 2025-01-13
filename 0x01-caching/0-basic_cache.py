#!/usr/bin/python3
"""
module: 0-basic_cache
description: inherits from BaseCaching class.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ @description
    Attributes:
    Methods:
    """
    def put(self, key, item):
        """adds an item to cache system"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Extracts items by key"""
        return self.cache_data.get(key, None)
