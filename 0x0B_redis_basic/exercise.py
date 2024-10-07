#!/usr/bin/env python3
import redis
import uuid
from typing import Union

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
