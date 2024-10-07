#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """
    A Cache class that interfaces with Redis to store and retrieve data.
    """

    def __init__(self):
        """
        Initializes a new Cache instance with a Redis client and clears the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The data is stored in Redis with the generated key as the identifier. The key is
        returned so it can be used to retrieve the data later.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieves the data stored in Redis for the given key, with an optional transformation function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves the data as a UTF-8 string for the given key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the data as an integer for the given key.
        """
        return self.get(key, fn=int)
