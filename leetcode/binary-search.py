from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return -1

s = Solution()

l = list(range(0,16))
for i in l:
    assert s.search(l, i) == i

assert s.search(l, -1) == -1
assert s.search(l, 16) == -1
