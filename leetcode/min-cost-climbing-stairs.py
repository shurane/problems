from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mc0 = cost[0]
        mc1 = cost[1]


        for c in cost[2:]:
            nextMinCost = mc1
            mc1 = min(mc0, mc1) + c
            mc0 = nextMinCost

        return min(mc0, mc1)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        prev = cost[~0]
        curr = cost[~1]
        for i in range(2, len(cost)):
            temp = min(prev, curr) + cost[~i]
            prev = curr
            curr = temp

        return min(prev, curr)

s = Solution()
assert s.minCostClimbingStairs([10, 15, 20]) == 15
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert s.minCostClimbingStairs([0, 1, 1, 0]) == 1

assert s.minCostClimbingStairs2([10, 15, 20]) == 15
assert s.minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert s.minCostClimbingStairs2([0, 1, 1, 0]) == 1