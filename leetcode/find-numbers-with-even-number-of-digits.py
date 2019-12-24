from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digits = 0
            while num > 0:
                num = num // 10
                digits += 1

            if digits % 2 == 0:
                count += 1

        return count

s = Solution()

assert s.findNumbers([12,345,2,6,7896]) == 2
assert s.findNumbers([]) == 0
assert s.findNumbers([555,901,482,1771]) == 1
assert s.findNumbers([1234,5678,9012,3456]) == 4