from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # this problem is kind of annoying. IMO there's not much of a clean solution to it. Maybe there's a clever way using a stack or heap?
        # https://leetcode.com/problems/non-decreasing-array/discuss
        # https://leetcode.com/problems/non-decreasing-array/discuss/106842/The-easiest-python-solution

        # there are also ways to do this by modifying the original array based on which of the two elements to change
        gt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                gt += 1
                # check left (i-1, i+1) and right (i, i+2) sides to make sure they are not also decreasing
                if i-1 >= 0         and nums[i-1] > nums[i+1] and \
                   i+2 <  len(nums) and nums[i]   > nums[i+2]:
                    return False

        # print(nums, gt, gt < 2)
        return gt < 2

s = Solution()

assert s.checkPossibility([4,2,3]) == True
assert s.checkPossibility([4,2,1]) == False
assert s.checkPossibility([1,2,1,1]) == True
assert s.checkPossibility([3,2,3,3]) == True
assert s.checkPossibility([3,2,4,3]) == False
assert s.checkPossibility([5,7,1,8]) == True
assert s.checkPossibility([3,4,2,5]) == True
assert s.checkPossibility([3,4,2,3]) == False