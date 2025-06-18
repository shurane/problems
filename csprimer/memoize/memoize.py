import urllib.request
from http.client import HTTPResponse
import json
import time
from typing import TypeVar
from collections.abc import Callable

T = TypeVar("T")
# very similar to a decorator but more like a higher order function, since we're interested in the result
# found while looking up different ways to time in python from https://builtin.com/articles/timing-functions-python
# there's time.perf_counter(), time.time(), timeit module (which doesn't preserve the return value), and cProfile/profile
def time_perf_counter(func: Callable[[], T]) -> tuple[T, float]:
    start = time.perf_counter()
    result = func()
    end = time.perf_counter()
    elapsed = end - start
    return (result, elapsed)


def memoize(func: Callable[..., T]) -> Callable[..., T]:
    lookup = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in lookup:
            return lookup[key]

        lookup[key] = func(*args, **kwargs)
        return lookup[key]
    return wrapper

@memoize
def fetch(url: str) -> str:
    response: HTTPResponse
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        return content

@memoize
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = 100
for i in range(n):
    result, elapsed = time_perf_counter(lambda: fib(i))
    print(f"fib({i}) == {result}, elapsed={elapsed}")

for i in range(n):
    content = fetch("https://httpbin.org/uuid")
    data = json.loads(content)
    uuid = data["uuid"]
    print(f"request #{i:3}: , {uuid}")
