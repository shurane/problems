class Solution:
    def binarySearch(self, nums, lo, hi, target):
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(lo, mid, hi)
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

    def search(self, nums, target):
        # see https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
        # I don't quite know how this works...
        if not nums:
            return -1

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            # print("before", lo, mid, hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        split = lo

        # print("split", split)

        # TODO why doesn't this work?
        # if nums[0] <= target <= nums[split]:
        #     return self.binarySearch(nums, 0, split, target)
        # else:
        #     return self.binarySearch(nums, split, len(nums) - 1, target)


        left = self.binarySearch(nums, 0, split, target)
        if left >= 0:
            return left

        right = self.binarySearch(nums, split, len(nums) - 1, target)
        if right >= 0:
            return right

        return -1

s = Solution()

assert(s.search([], 5) == -1)
assert(s.search([8,9,2,3,4], 9) == 1)
assert(s.search([8,1,2,3,4,5,6,7], 8) == 0)
assert(s.search([2,3,4,5,6,7,8,1], 8) == 6)
assert(s.search([5,6,7,8,1,2,3,4], 8) == 3)
assert(s.search([8,1,2,3,4,5,6,7], 9) == -1)
assert(s.search([4,5,6,7,0,1,2], 0) == 4)
assert(s.search([4,5,6,7,0,1,2], 3) == -1)
assert(s.search([4,5,6,7,8,1,2,3], 8) == 4)