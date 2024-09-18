#!/usr/bin/python3
from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRU caching system """
    
    def __init__(self):
        """ Initialize LRUCache class """
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        """ Add an item to the cache """
        