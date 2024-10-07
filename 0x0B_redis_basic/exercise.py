#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments the call count in Redis each time the method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


class Cache:
    """
    A class that provides an interface to store and retrieve data using Redis.
    """

    def __init__(self):
        """
        Initializes the Cache with a Redis client and clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a UUID key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieves data from Redis for a given key, with optional transformation.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data as a UTF-8 string for a given key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data as an integer for a given key.
        """
        return self.get(key, fn=int)
