# for i in range(20):
#     total = i * (i-1) // 2
#     print(sum(range(0,i)), total)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # see triangular numbers, or sum of first n natural numbers, or https://oeis.org/A000217
        total = n * (n+1) // 2
        missing = 0
        for i in nums:
            missing += i
        # print(total, missing)
        return total - missing

s = Solution()
assert s.missingNumber([3,0,1]) == 2
assert s.missingNumber([0,2]) == 1
assert s.missingNumber([0,1]) == 2