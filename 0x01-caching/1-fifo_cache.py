#!/usr/bin/python3
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache (First-In-First-Out Cache) implementation.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, the least recently used item
        will be discarded.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Returns the item if found, else None.
        """
        return self.cache_data.get(key)
