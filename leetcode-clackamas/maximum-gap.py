from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # apparently this is radix sort
        # see https://leetcode.com/problems/maximum-gap/discuss/1240543/Python-Bucket-sort-explained
        if len(nums) <=2: return 0
