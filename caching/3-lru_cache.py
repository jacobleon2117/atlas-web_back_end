#!/usr/bin/python3
"""
LIFOCache module - caching system using LIFO (Last In First Out) algorithm.
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the class with an empty cache and track insertion order. """
        super().__init__()
        self.order = []  # To track the insertion order

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds the limit, discard the most recently added item (LIFO).
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()  # Remove last added item
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Return the value in the cache linked to key or None if not found. """
        return self.cache_data.get(key, None)
