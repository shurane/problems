from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2

        while lo < hi:
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                # print("found target")
                # print(mid, nums[mid])
                break
            mid = (lo + hi) // 2

        if nums[mid] != target: return [-1, -1]

        lo = 0
        hi = mid
        left = (lo + hi) // 2
        # print("before", lo, left, hi)
        while lo < hi:
            if target == nums[left]:
                hi = max(left - 1, 0)
            else:
                lo = left + 1
            left = (lo + hi) // 2

        # print(" after", lo, left, hi)

        lo = mid
        hi = len(nums) - 1
        right = (lo + hi) // 2
        while lo < hi:
            if target == nums[right]:
                lo = right + 1
            else:
                hi = right - 1
            right = (lo + hi) // 2

        if nums[left] != target:
            left += 1
        if nums[right] != target:
            right -= 1

        # print(left, right)
        return [left, right]

s = Solution()
assert s.searchRange([3,3,3], 3) == [0, 2]
assert s.searchRange([3,3,3,3], 3) == [0, 3]
assert s.searchRange([3,3,3,3,3], 3) == [0, 4]
assert s.searchRange([8,8,8,8,8,8], 8) == [0, 5]
assert s.searchRange([1,8,8,8,8,8,8,10], 8) == [1, 6]
assert s.searchRange([0,1,2,3,4,5,6,7,8,9,10], 8) == [8,8]
assert s.searchRange([0,1,2,3,4,5,6,7,8,9,10], 4) == [4,4]
assert s.searchRange([5,7,7,8,8,10], 8) == [ 3,  4]
assert s.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
assert s.searchRange([], 0) == [-1, -1]