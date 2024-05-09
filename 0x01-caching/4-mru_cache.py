#!/usr/bin/python3
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching



class MRUCache(BaseCaching):
    """
    Implements a MRU (Most Recently Used) cache.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.order = []  # List to keep track of the order of access

    def put(self, key, item):
        """
        Adds an item to the cache. If the cache is full, the least
        recently used item is discarded.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)  # Add the new item at the end

    def get(self, key):
        """
        Retrieves an item from the cache. If the item exists,
        it is moved to the end of the order list to reflect
        its recent use.
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
