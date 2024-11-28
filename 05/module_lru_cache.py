from collections.abc import Hashable


class LRUCache:
    def __init__(self, limit=42):
        if not isinstance(limit, int):
            raise TypeError("limit must be 'int'")
        if limit < 0:
            raise ValueError("limit must be positive")
        self.limit = limit
        self.cache = {}

    def get(self, key):
        if not isinstance(key, Hashable):
            raise KeyError("key must be hashable")
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return None

    def set(self, key, value):
        if not isinstance(key, Hashable):
            raise KeyError("key must be hashable")
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.limit:
                del self.cache[next(iter(self.cache))]
            self.cache[key] = value
