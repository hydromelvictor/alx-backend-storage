#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument
and returns a string. The method should generate
a random key (e.g. using uuid), store the input data
in Redis using the random key and return the key.

Type-annotate store correctly.
Remember that data can be a str, bytes, int or float.
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps
import sys


def count_calls(method: Callable) -> Callable:
    """
    f : callable
    return : callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        arguments list or dict
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call history
    """
    key = method.__qualname__
    entry = key + ":inputs"
    out = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        list or dict
        """
        self._redis.rpush(entry, str(args))
        outer = method(self, *args, **kwargs)
        self._redis.rpush(out, str(outer))
        return outer
    return wrapper


class Cache:
    """
    class cache
    """
    def __init__(self):
        """
        init method
        return : none
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    @call_history
    def store(self, data: Union[str, int, bytes, float]) -> str:
        """
        return id redis new entry create
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        """
        key : str
        fn : option Callable
        return Callable
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self) -> str:
        """
        string
        """
        return self.decode("utf-8")

    def get_int(self) -> int:
        """integer"""
        return int.from_bytes(self, sys.byteorder)
