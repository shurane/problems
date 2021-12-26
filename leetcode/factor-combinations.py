from typing import List
from unittest import TestCase
import math

tc = TestCase()

class Solution:
    def getFactorsMoreRecursive(self, n: int) -> List[List[int]]:
        # Elegant looking solution (based on combination sum and related questions)
        # But results in a stack overflow for the call stack, so not at all ideal here
        if n == 1: return []

        def helper(i, top):
            if top == 1:
                results.append(list(values))
                return

            elif i > top: return

            helper(i + 1, top)

            if top % i == 0 and i != n:
                values.append(i)
                helper(i, top // i)
                values.pop()

        results = []
        values = []
        helper(2, n)

        return results

    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1: return []

        def helper(i, target):
            # print("helper", i, target, values)
            if target == 1:
                if len(values) > 1:
                    # print("answer", values)
                    results.append(list(values))
                return
            j = i
            # hint from https://leetcode.com/problems/factor-combinations/, uses square root to keep it quite fast
            while j*j <= target:
                if target % j == 0:
                    values.append(j)
                    helper(j, target // j)
                    values.pop()
                j += 1

            # also adds 'target' as a value. So should be able to get numbers above square root as a factor, like n / 2
            values.append(target)
            helper(n, 1)
            values.pop()

        results = []
        values = []
        helper(2, n)

        # print(results, len(results))
        return results

    def getFactorsShort(self, n: int) -> List[List[int]]:
        # answer gleaned from one of the solutions on the submission graph
        # very clever usage of an empty array so only need one condition
        self.res = []

        def solver(n, start, now):
            if now:
                self.res.append(now+[n])
            end = int(math.sqrt(n))+1
            for i in range(start, end):
                if n%i==0:
                    solver(int(n/i), i, now+[i])

        solver(n,2,[])
        return self.res

s = Solution()
assert s.getFactors(1) == []
assert s.getFactors(2) == []
assert s.getFactors(3) == []
assert s.getFactors(4) == [[2,2]]
tc.assertCountEqual(s.getFactors(12), [[2,6],[3,4],[2,2,3]])

# http://oeis.org/A004394 - superabundant numbers
# assert len(s.getFactors(25200)) == 1149
# assert len(s.getFactors(55440)) == 1762
# assert len(s.getFactors(166320)) == 4322
# assert len(s.getFactors(8648640)) == 88578

assert len(s.getFactorsShort(25200)) == 1149
assert len(s.getFactorsShort(55440)) == 1762
assert len(s.getFactorsShort(166320)) == 4322
assert len(s.getFactorsShort(8648640)) == 88578