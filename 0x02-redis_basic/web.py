#!/usr/bin/env python3
"""
Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching.
"""
import requests
from typing import Callable
from functools import wraps
import redis


def decoration(method: Callable) -> Callable:
    """
    methode callable
    """
    key = "count:{}".format(url)
    cache = "cached:{}".format(url)

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        text = method(self, *args, **kwargs)
        redis.setex(cache, 10, text)
        return text
    return wrapper


@decoration
def get_page(url: str) -> str:
    """
    url : str
    return : str
    """
    rep = requests.get(url)
    return rep.text
