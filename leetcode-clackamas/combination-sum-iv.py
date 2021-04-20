from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # see https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question
        # also https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation
        # what is the difference between top down and bottom up? I guess I can kind of understand, and I think I've used it for another problem
        # this also looks pretty similar to https://leetcode.com/problems/coin-change/
        nums = sorted(nums)
        counts = [0 for i in range(target + 1)]
        counts[0] = 1

        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    counts[i] += counts[i - j]

        # print(target, nums, counts)
        return counts[-1]



s = Solution()
assert s.combinationSum4([1], 4) == 1
assert s.combinationSum4([1,2], 4) == 5
assert s.combinationSum4([1,2,3], 4) == 7
assert s.combinationSum4([1,2,3,4], 4) == 8
assert s.combinationSum4([9], 3) == 0