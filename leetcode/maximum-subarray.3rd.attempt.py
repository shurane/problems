from typing import List

class Solution:
    def maxSubArrayON(self, nums: List[int]) -> int:
        sums = [nums[0] for num in nums]
        m = nums[0]

        i = 1
        while i < len(nums):
            if nums[i] > sums[i-1] + nums[i]:
                sums[i] = nums[i]
            else:
                sums[i] = sums[i-1] + nums[i]

            if sums[i] > m:
                m = sums[i]
            i += 1


        return m

    def maxSubArray(self, nums: List[int]) -> int:

        prev = nums[0]
        currentMax = nums[0]

        i = 1
        while i < len(nums):
            temp = None

            if nums[i] > prev + nums[i]:
                temp = nums[i]
            else:
                temp = prev + nums[i]

            currentMax = max(prev, currentMax)
            prev = temp

            i += 1

        return max(prev, currentMax)
