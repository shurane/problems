from typing import List

class Solution:
    def searchInsert2(self, nums: List[int], target: int) -> int:
        # I can't believe I wrote all these weird corner cases.. kind of sad to see
        # I guess this happens when I chase one case after another. Kind of like whack-a-mole
        lo, hi = 0, len(nums) - 1

        if not nums:
            return 0
        elif target < nums[lo]:
            return lo
        elif target > nums[hi]:
            return len(nums)
        elif lo == hi:
            if target > nums[lo]:
                return 1
            else:
                return 0

        while lo <= hi:
            mid = (lo + hi) // 2
            # print(lo, hi, mid)
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid

        # lo >= hi
        # print("outside")
        if target < nums[mid]:
            return mid
        else:
            return mid + 1


    def searchInsert(self, nums: List[int], target: int) -> int:
        # referring to https://leetcode.com/problems/search-insert-position/discuss/15080/My-8-line-Java-solution
        # I guess it makes more sense to return lo outside of the while loop instead of mid
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

s = Solution()
assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1
assert s.searchInsert([1,3,5,6], 7) == 4
assert s.searchInsert([1,3,5,6], 0) == 0
assert s.searchInsert([], 0) == 0
assert s.searchInsert([1], 2) == 1
assert s.searchInsert([1], 1) == 0
assert s.searchInsert([1], 0) == 0
assert s.searchInsert([1,3], 2) == 1
assert s.searchInsert([1,3,5], 1) == 0

# took over an hour, and had to refer to other solutions after solving to switch from searchInsert2() to searchInsert()
