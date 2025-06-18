import urllib.request
import time
from typing import Any

# TODO type hints could be a bit better with U, V, etc.
def time_perf_counter(f, *args) -> tuple[Any, float]:
    start = time.perf_counter()
    result = f(*args)
    end = time.perf_counter()
    elapsed = end - start
    return (result, elapsed)


def memoize(f, lookup, *args):
    if args in lookup:
        return lookup[args]

    lookup[args] = f(*args)
    return lookup[args]

def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

lookup = {}
n = 35
for i in range(n):
    result, elapsed = time_perf_counter(lambda: memoize(fib, lookup, n))
    print(f"fib({n}) == {result}, elapsed={elapsed}")

print(fetch('http://google.com')[:80])
