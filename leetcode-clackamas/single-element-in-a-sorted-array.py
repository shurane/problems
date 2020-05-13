from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # how to take advantage of the array being sorted?
        value = nums[0]
        for elem in nums[1:]:
            value ^= elem

        return value


    def singleNonDuplicateBinary(self, nums: List[int]) -> int:
        # this is too complicated... and incidentally, doesn't work
        print(f"singleNonDuplicateBinary({nums})")
        lo = 0
        hi = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while lo < hi - 2:
            mid = (lo + hi) // 2
            print(f"lo: {lo}, mid: {mid}, hi: {hi}, nums[mid-1]: {nums[mid-1]}, nums[mid]: {nums[mid]}, nums[mid+1]: {nums[mid+1]}")
            if nums[mid] == nums[mid+1]:
                if len(nums) % 4 == 3:
                    print("switching left")
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] == nums[mid-1]:
                if len(nums) % 4 == 3:
                    print("switching right")
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                return nums[mid]

        if nums[lo] == nums[lo+1]:
            return nums[lo+2]
        elif nums[lo+1] == nums[lo+2]:
            return nums[lo]
        else:
            return nums[lo+1]

        return None

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100754/Java-Binary-Search-short-(7l)-O(log(n))-w-explanations
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1: ## lines up on an even index for mid
                mid-=1

            if nums[mid] != nums[mid+1]: ## the pair doesn't line up, look left
                hi = mid
            else:
                lo = mid + 2 # look 2 past the pair

        return nums[lo]


s = Solution()

assert s.singleNonDuplicate([1]) == 1
assert s.singleNonDuplicate([1,3,3]) == 1
assert s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
assert s.singleNonDuplicate([3,3,7,7,10,11,11]) == 10

assert s.singleNonDuplicate2([1]) == 1
assert s.singleNonDuplicate2([1,3,3]) == 1
assert s.singleNonDuplicate2([1,1,3]) == 3
assert s.singleNonDuplicate2([1,1,2,3,3,4,4,8,8]) == 2
assert s.singleNonDuplicate2([1,1,3,3,4,4,5,8,8]) == 5
assert s.singleNonDuplicate2([1,1,3,3,4,5,5,8,8]) == 4

assert s.singleNonDuplicate2([0,1,1,3,3]) == 0
assert s.singleNonDuplicate2([1,1,2,3,3]) == 2
assert s.singleNonDuplicate2([1,1,3,3,4]) == 4

assert s.singleNonDuplicate2([0,1,1,3,3,5,5]) == 0
assert s.singleNonDuplicate2([1,1,2,3,3,5,5]) == 2
assert s.singleNonDuplicate2([1,1,3,3,4,5,5]) == 4
assert s.singleNonDuplicate2([1,1,3,3,5,5,6]) == 6

assert s.singleNonDuplicate2([0,1,1,3,3,5,5,7,7]) == 0
assert s.singleNonDuplicate2([1,1,2,3,3,5,5,7,7]) == 2
assert s.singleNonDuplicate2([1,1,3,3,4,5,5,7,7]) == 4
assert s.singleNonDuplicate2([1,1,3,3,5,5,6,7,7]) == 6
assert s.singleNonDuplicate2([1,1,3,3,5,5,7,7,8]) == 8

assert s.singleNonDuplicate2([0,1,1,3,3,5,5,7,7,9,9]) == 0
assert s.singleNonDuplicate2([1,1,3,3,5,5,7,7,9,9,10]) == 10

assert s.singleNonDuplicate2([3,3,7,7,10,11,11]) == 10
