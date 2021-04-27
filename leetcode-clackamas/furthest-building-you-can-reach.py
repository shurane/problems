from typing import List
from heapq import heappop, heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # from https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918374/Basic-Priority-Queue-Single-Pass-or-Code-with-Comments-or-Corner-Cases
        used = 0
        s = []

        for i in range(len(heights) - 1):
            if heights[i+1] < heights[i]:
                continue

            diff = heights[i+1] - heights[i]

            if used + diff <= bricks:
                used += diff
                heappush(s, -diff)
            elif ladders > 0:
                if s and -s[0] > diff:
                    # print("using a ladder and removing", -s[0], "bricks")
                    used -= -s[0] - diff
                    heappop(s)
                    heappush(s, -diff)
                ladders -= 1
            else:
                return i

            # print(f"{i:2}, {heights[i]:3} to {heights[i+1]:3}, bricks used: {used-diff:3} + {diff:3} to {used:3}, ladders left: {ladders:2}, heap:{s}")

        return len(heights) - 1

s = Solution()

assert s.furthestBuilding([10,9,8,7,6,5,4,3,2,1], 0, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 0, 5) == 5
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 10, 0) == 9
assert s.furthestBuilding([1,4,9,16,25,36,49,64,81,100], 99, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 9, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 5, 0) == 5
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 0, 10) == 9

assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 0, 10) == 9
assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 10, 0) == 5
assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 10, 5) == 9

assert s.furthestBuilding([1,51, 101], 0, 2) == 2
assert s.furthestBuilding([1,51, 101], 50, 1) == 2
assert s.furthestBuilding([1,51, 101], 100, 0) == 2
assert s.furthestBuilding([1,51, 101], 50, 0) == 1
assert s.furthestBuilding([1,51, 101], 0, 1) == 1
assert s.furthestBuilding([1,51, 101], 49, 1) == 1

assert s.furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4
assert s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7
assert s.furthestBuilding([14,3,19,3], 17, 0) == 3