from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC%2B%2BPython-Backtrack-OJ-is-wrong
        # interesting solution...
        total = sum(target)
        A = [-i for i in target]
        heapq.heapify(A)

        while True:
            a = -heapq.heappop(A)
            total -= a

            if a == 1 or total == 1: return True

            # why does it matter if total == 0? and what's a % total checking?
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)

s = Solution()
assert s.isPossible([9,3,5]) == True
assert s.isPossible([8,5]) == True
assert s.isPossible([1,1,1,2]) == False
assert s.isPossible([1,100]) == True
assert s.isPossible([1,1000]) == True
assert s.isPossible([1,10e9]) == True
