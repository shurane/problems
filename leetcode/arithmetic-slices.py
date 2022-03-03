from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0

        matches = 0
        diffs = []
        j = 0
        for i in range(1, len(nums)):
            diffs.append(nums[i] - nums[i-1])

            if i - j >= 2 and diffs[-1] == diffs[j]:
                matches += 1 # new match
                matches += i - j - 2 # subarrays

            if diffs[-1] != diffs[j]:
                j = len(diffs) - 1

        return matches

    # https://leetcode.com/problems/arithmetic-slices/solution/
    # technically it's DP, but it made more sense for me to rename the variables
    def numberOfArithmeticSlicesDP(self, nums: List[int]) -> int:
        length = 0
        total = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                length += 1
                total += length
            else:
                length = 0
        return total

s = Solution()
cases = ([[1], 0],
         [[1,2,3,4], 3],
         [[1,2,3,4,5], 6],
         [[1,2,3,4,5,6], 10],
         [[1,2,3,4,7,7,7,7], 6],
         [[1,2,3,4,5,7,7,7,7,7], 12])

for case, expected in cases:
    assert s.numberOfArithmeticSlices(case) == expected
    assert s.numberOfArithmeticSlicesDP(case) == expected
