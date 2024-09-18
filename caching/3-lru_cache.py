#!/usr/bin/python3
""" LRUCache - module that inherits from BaseCaching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ 
        LRUCache implements a caching system with
        the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """ 
            Initialize the LRUCache class with
            a list to track the order of usage.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ 
            Add an item to the cache using the LRU algorithm.
            If the cache exceeds the MAX_ITEMS,
            discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)

        self.cache_data[key] = item
        self.lru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
            Retrieve an item from the
            cache based on the key.
        """

        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
