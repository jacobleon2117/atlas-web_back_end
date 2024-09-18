#!/usr/bin/python3
""" FIFOCache module that inherits from BaseCaching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implements a caching system using FIFO algorithm """

    def __init__(self):
        """ Initialize the class with an empty cache
        and a queue to track order of keys """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache using FIFO """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first item in the queue (FIFO)
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item by key from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
