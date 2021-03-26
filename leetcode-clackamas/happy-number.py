from typing import Iterable
from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            temp = reduce(lambda acc, x: acc + x*x, reversedDigits(n), 0)
            # print(f"current: {n:4}, next:{temp:4}")
            n = temp

        # print(visited, n)
        return n == 1

def reversedDigits(num: int) -> Iterable[int]:
    # d = []
    while num > 1:
        # d.append(num % 10)
        yield num % 10
        num = num // 10
    # d.append(num)
    yield num

# print(list(reversedDigits(0)))
# print(list(reversedDigits(1)))
# print(list(reversedDigits(5)))
# print(list(reversedDigits(12)))
# print(list(reversedDigits(123)))
# print(list(reversedDigits(1234)))
# print(list(reversedDigits(12345)))
# print(list(reversedDigits(100)))

s = Solution()
assert s.isHappy(1) == True
assert s.isHappy(19) == True
assert s.isHappy(16) == False