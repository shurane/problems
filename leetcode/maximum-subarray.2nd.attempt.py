from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force would be O(n**2), compute the sume for all i,j values of the list and get the max sum
        # how to do O(n)?

        sums = [num for num in nums]
        highest = nums[0]

        i = 1
        while i < len(nums):
            update = sums[i-1] + nums[i]
            if update > sums[i]:
                sums[i] = update
            if sums[i] > highest:
                highest = sums[i]
            i += 1

        # print(sums, highest)
        return highest

s = Solution()

s.maxSubArray([1,1,1,1,1,1,1,1,1,1])
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

assert s.maxSubArray([1]) == 1
assert s.maxSubArray([1,2,3]) == 6
assert s.maxSubArray([1,-2,3]) == 3
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert s.maxSubArray([500,-1,-1,-1,-1,500]) == 996
