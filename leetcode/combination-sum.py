from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        results = []
        combination = []

        def helper(i: int, k: int):
            if k == target:
                results.append(combination[:])
                return
            elif i == len(candidates):
                return

            if k + candidates[i] <= target:
                combination.append(candidates[i])
                helper(i, k + candidates[i])
                combination.pop()

            helper(i+1, k)

        helper(0, 0)
        return results


s = Solution()

assert s.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
assert s.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
assert s.combinationSum([2], 1) == []
