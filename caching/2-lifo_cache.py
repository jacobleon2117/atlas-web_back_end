#!/usr/bin/python3
""" LIFOCache - module that inherits from BaseCaching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system where the last added item is the first to be removed
        when the cache exceeds its size limit. """

    def __init__(self):
        """ Initialize the LIFOCache class with a tracking list 'order' to manage
            the insertion order of the cache items. """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache. If the cache exceeds the maximum allowed size,
            it removes the last added item (LIFO). 
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.order:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key."""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
