from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # base case with 1 element
        # otherwise, sort the list and count the number of elements
        # if count for a value is greater than n // 2, then return that
        # run time: O(nlogn), space: O(1)

        if len(nums) == 1:
            return nums[0]

        ordered = sorted(nums)
        i = 0
        count = 0
        while i < len(ordered) - 1:
            if ordered[i] != ordered[i+1]:
                count = 0
            count += 1

            if count > len(nums) // 2:
                return ordered[i]

            i += 1
        return None

    def majorityElement2nd(self, nums: List[int]) -> int:
        # Uses O(n) space in exchange for amortized O(n) time
        counts = dict()
        for element in nums:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

            if counts[element] > len(nums) // 2:
                return element

        return None

s = Solution()

assert s.majorityElement2nd([0]) == 0
assert s.majorityElement2nd([3,2,3]) == 3
assert s.majorityElement2nd([2,2,1,1,1,2,2]) == 2

# [1,1,1,1,2,2,3,3] would not be a valid input.
# A majority element would show up **more than** n // 2 times
# note: https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
# very cool solution for O(1) space and O(n) time, based on "Boyer-Moore Majority Vote Algorithm"