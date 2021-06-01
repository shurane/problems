from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-erasure-value/discuss/978608/Python3-O(n)-sliding-window
        best = 0
        cumulative = 0
        seen = set()

        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cumulative -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            cumulative += nums[j]
            best = max(best, cumulative)

        return best

s = Solution()
assert s.maximumUniqueSubarray([4,2,4,5,6]) == 17
assert s.maximumUniqueSubarray([10,10,10,10,10,10]) == 10