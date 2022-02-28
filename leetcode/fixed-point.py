from typing import List

class Solution:
    # simple, but slow, O(n)
    def fixedPointLinear(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1

    # O(log n), clever idea
    def fixedPoint(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        lowest = len(arr)

        while lo <= hi:
            i = (lo + hi) // 2
            if arr[i] < i:
                lo = i + 1
            elif arr[i] > i:
                hi = i - 1
            else:
                lowest = min(lowest, i)
                # can still have a lower fixed point, so keep checking left
                hi = i - 1

        if lowest == len(arr):
            return -1
        return lowest

s = Solution()
cases = [([-10,-5,0,3,7], 3),
         ([0,2,5,8,17], 0),
         ([-10,-5,3,4,7,9], -1),
         ([-10,-5,-2,0,4,5,6,7,8,9,10], 4)]

for array, expected in cases:
    assert s.fixedPointLinear(array) == expected
    assert s.fixedPoint(array) == expected
