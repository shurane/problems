from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # find starting point of the cycle. See https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow

s = Solution()

assert s.findDuplicate([1,3,4,2,2]) == 2
assert s.findDuplicate([3,1,3,4,2]) == 3

assert s.findDuplicate([1,1,1,1,2]) == 1
assert s.findDuplicate([4,3,1,4,2]) == 4