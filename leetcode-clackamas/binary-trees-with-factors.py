from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = sorted(arr)
        amounts = dict((elem, 0) for elem in s)
        # print("before", amounts)

        i = 0
        while i < len(s):
            j = 0

            while s[j] <= s[i] // 2:
                si = s[i]
                sj = s[j]
                # print(si, sj)
                if si % sj == 0 and (si // sj) in amounts:
                    # print(si, sj, si // sj, "found a pair")
                    amounts[si] += amounts[sj] * amounts[si // sj]
                j += 1

            amounts[s[i]] += 1

            i += 1

        # print(amounts)
        return sum(amounts.values()) % (10**9 + 7)

s = Solution()

assert s.numFactoredBinaryTrees([2]) == 1
assert s.numFactoredBinaryTrees([5]) == 1
assert s.numFactoredBinaryTrees([2, 4]) == 3
assert s.numFactoredBinaryTrees([2, 4, 5, 10, 20]) == 18
assert s.numFactoredBinaryTrees([2, 4, 5, 10, 50]) == 14