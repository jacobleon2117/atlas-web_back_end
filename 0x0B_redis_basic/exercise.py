#!/usr/bin/env python3
"""
    Redis Basic: module
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments the call count
    in Redis each time the method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the input
    parameters and output for a function call in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(outputs_key, output)

        return output

    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the history of calls for a particular function.
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    call_count = len(inputs)
    print(f"{method.__qualname__} was called {call_count} times:")

    for inp, out in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{inp.decode('utf-8')}) -> "
            f"{out.decode('utf-8')}"
        )


class Cache:
    """
    A class that provides an interface to store
    and retrieve data using Redis.
    """

    def __init__(self):
        """
        Initializes the Cache with a Redis client
        and clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self,
              data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a UUID key
        and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None
    ) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieves the data stored in Redis for the given key,
        with an optional transformation function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

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
