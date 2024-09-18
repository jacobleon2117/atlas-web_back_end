#!/usr/bin/python3
""" MRUCache - module that inherits from BaseCaching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        MRUCache implements a caching system with
        the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """
            Initialize the MRUCache class
            with a list to track the order of usage.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
            Add an item to the cache using the MRU algorithm.
            If the cache exceeds the MAX_ITEMS,
            discard the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)

        self.cache_data[key] = item
        self.mru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
            Retrieve an item from the cache based on the key.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]
