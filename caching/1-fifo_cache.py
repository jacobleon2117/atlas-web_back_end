#!/usr/bin/python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """
    
    
    def __init__(self):
        """ Initialize FIFOCache class """
        super().__init__()
        self.order = []
    
    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: [oldest_key]")
                
        self.cache_data[key] = item
        self.order.append(key)
    
    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
