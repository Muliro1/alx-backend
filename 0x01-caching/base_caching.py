#!/usr/bin/python3
""" BaseCaching module
"""



class BaseCaching():
    """
    BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    # Maximum number of items allowed in the cache.
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache."""
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache.

        Prints the current cache in the format:
        <key>: <value>
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        Add an item in the cache.

        If the cache is full, the least recently used item will be discarded.

        Args:
            key (str): The key for the item.
            item: The item to be added to the cache.

        Raises:
            NotImplementedError: This method must be implemented in the derived class.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item if found, else None.

        Raises:
            NotImplementedError: This method must be implemented in the derived class.
        """
        raise NotImplementedError("get must be implemented in your cache class")
