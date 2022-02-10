from typing import List

class Solution:
    # Initially attempted using 2 pointers. But ooks like 2 pointers is a bad fit for this problem.
    # The subproblems don't contribute to the bigger problem. Apparently negative numbers aren't great for this
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/301242/General-summary-of-what-kind-of-problem-can-cannot-solved-by-Two-Pointers
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/102114/Is-it-possible-to-solve-this-using-two-pointers
    # prefix sum plus a hash map. So simple.
    def subarraySum(self, nums: List[int], k: int) -> int:
        history = {0: 1}
        total = 0
        hits = 0

        for i in range(len(nums)):
            total += nums[i]
            if total - k in history:
                hits += history[total - k]

            if total in history:
                history[total] += 1
            else:
                history[total] = 1

        # print(nums, history, hits)
        return hits

s = Solution()
assert s.subarraySum([1], 1) == 1
assert s.subarraySum([1], 2) == 0
assert s.subarraySum([1,1], 2) == 1
assert s.subarraySum([1,1,0,0,0], 2) == 4
assert s.subarraySum([0,0,0,1,1], 2) == 4
assert s.subarraySum([0,0,1,1,0,0], 2) == 9
assert s.subarraySum([0,0,0,1,1,0,0,0], 2) == 16

assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3], 3) == 2