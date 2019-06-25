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

    # ok... i don't really understand this so I'll need to revisit this.
    # see https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110104/Easy-to-understand-Python-solution-O(1)-space

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        totalCosts = [0 for _ in cost]
        totalCosts[0] = cost[0]
        totalCosts[1] = min(cost[0], cost[1])


        for i in range(2, len(cost)):
            totalCosts[i] = min(totalCosts[i-1], totalCosts[i-2]) + cost[i]

        finalCost = min(totalCosts[-1], totalCosts[-2])
        print(totalCosts, finalCost)
        return finalCost

        # why doesn't minCostClimbingStairs2() work?

s = Solution()
assert s.minCostClimbingStairs([10, 15, 20]) == 15
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert s.minCostClimbingStairs([0, 1, 1, 0]) == 1