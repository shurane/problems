from typing import List

class Solution:
    def minMoves2_orig(self, nums: List[int]) -> int:
        nums = sorted(nums)

        # it seems like this isn't that important? But not sure why...
        if len(nums) % 2 == 1:
            median = nums[len(nums)//2]
        else:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
            if int(median + 0.5) != median:
                median += 1
            median = int(median)

        diff = 0
        for n in nums:
            diff += abs(n - median)

        # print(median, diff)
        return diff

    def minMoves2(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)

s = Solution()
assert s.minMoves2([0,10]) == 10
assert s.minMoves2([0,1,10]) == 10
assert s.minMoves2([1,2,3]) == 2
assert s.minMoves2([1,10,2,9]) == 16
assert s.minMoves2([1,1,1,1,9]) == 8
assert s.minMoves2([1,1,1,9]) == 8
assert s.minMoves2([1,1,1,100]) == 99
assert s.minMoves2([1,2,100]) == 99
assert s.minMoves2([1,1,1,10,10,10,10,100]) == 117