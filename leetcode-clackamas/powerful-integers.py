from typing import List
from math import log

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        elems = set()
        # interesting idea to use log to find the upper bound. See https://leetcode.com/problems/powerful-integers/solution/
        xbound = 1 if x == 1 else int(log(bound, x))
        ybound = 1 if y == 1 else int(log(bound, y))

        for i in range(xbound + 1):
            for j in range(ybound + 1):
                value = x ** i + y ** j
                if value <= bound:
                    elems.add(value)

        elems = sorted(elems)
        # print(x, y, bound, elems)
        return elems

s = Solution()
assert s.powerfulIntegers(1, 1, 1) == []
assert s.powerfulIntegers(1, 1, 10) == [2]
assert s.powerfulIntegers(2, 1, 10) == [2,3,5,9]
assert s.powerfulIntegers(1, 2, 10) == [2,3,5,9]
assert s.powerfulIntegers(2, 3, 10) == [2,3,4,5,7,9,10]
assert s.powerfulIntegers(3, 5, 15) == [2,4,6,8,10,14]