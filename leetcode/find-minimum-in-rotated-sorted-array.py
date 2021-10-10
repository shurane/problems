# import blessings
# term = blessings.Terminal()
from typing import List

# def colorized_array(arr, begin, mid, end):
    # result = ""
    # space = " "
    # for i in range(len(arr)):
        # if i == len(arr) - 1:
            # space = ""

        # r = "{: 3d}".format(arr[i])
        # if i == begin:
            # result += term.red(r) + space
        # elif i == end:
            # result += term.blue(r) + space
        # # sometimes mid might overlap with begin or end
        # elif i == mid:
            # result += term.green(r) + space
        # else:
            # result += str(r) + space
    # return result

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # isn't this the equivalent of finding the pivot and comparing that to
        # the leftmost element?
        begin = 0
        end = len(nums) - 1

        lowest = nums[begin]

        while begin <= end:
            mid = begin + (end - begin) // 2

            # carr = colorized_array(nums, begin, mid, end)
            # print "{: 3d}".format(begin), "{: 3d}".format(mid), "{: 3d}".format(end),
            # print "lowest:{: 3d}, nums:{}".format(lowest, carr)

            lowest = min(lowest, nums[begin], nums[mid], nums[end])

            # go down the half that isn't sorted
            if nums[begin] > nums[mid]:
                # left half unsorted
                end = mid - 1
            else:
                # right half unsorted
                begin = mid + 1
        return lowest

    def findMinRedo(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        else:
            lo = 0
            hi = len(nums) - 1
            # print("lhn  ", lo, hi, nums)
            if nums[lo] <= nums[hi]:
                return nums[lo]

            else:
                mid = (lo + hi) // 2
                minval = min(self.findMinRedo(nums[:mid]), self.findMinRedo(nums[mid:]))
                # print("lhmmn", lo, hi, mid, minval, nums)
                return minval

    def findMinDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        else:
            lo = 0
            hi = len(nums) - 1
            mid = (lo + hi) // 2
            if nums[lo] < nums[hi]:
                return nums[lo]
            else:
                return min(self.findMinDuplicates(nums[:mid]), self.findMinDuplicates(nums[mid:]))


s = Solution()
a1 = list(range(16))

for i in a1:
    # rotate the array around... should always return 0
    newA = a1[i:] + a1[:i]
    assert s.findMin(newA) == 0

assert s.findMinRedo([3,4,5,1,2]) == 1
assert s.findMinRedo([4,5,6,7,0,1,2]) == 0
assert s.findMinRedo([11,13,15,17]) == 11
assert s.findMinRedo([1,3,2]) == 1
assert s.findMinRedo([2,3,1]) == 1

# find-minimum-in-rotated-sorted-array-ii
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
assert s.findMinDuplicates([3,3,1,3]) == 1
assert s.findMinDuplicates([0,1,2,3,4,5,6,7,8,9]) == 0
assert s.findMinDuplicates([0,1,2,3,4,5,6,7,8,0]) == 0
assert s.findMinDuplicates([9,1,2,3,4,5,6,7,8,9]) == 1
assert s.findMinDuplicates([0,0,0,0,1,1,1,1]) == 0
assert s.findMinDuplicates([1,1,1,1,0,0,0,0]) == 0
assert s.findMinDuplicates([1,1,1,1,0,1,1,1]) == 0

# slowly convert the list from 1s to 0s
l1 = list(1 for i in range(100))
for i in range(100):
    l1[i] = 0
    assert s.findMinDuplicates(l1) == 0

# slowly move the 0 in the list of 1s from left to right
l2 = list(1 for i in range(100))
for i in range(100):
    l2[i] = 0
    l2[i-1] = 1
    assert s.findMinDuplicates(l2) == 0