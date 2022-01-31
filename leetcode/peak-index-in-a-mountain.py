from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # return A.index(max(A)) # O(n) solution

        # O (n log n) solution
        lo = 0
        hi = len(A)

        while lo < hi:
            mid = (lo + hi) // 2
            print(lo, mid, hi)
            if A[mid - 1] < A[mid] < A[mid + 1]:
                lo = mid
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                hi = mid
            else:
                return mid
                # A[mid - 1] < A[mid]
                # A[mid]     > A[mid + 1]
        return -1

s = Solution()
assert s.peakIndexInMountainArray([0,1,0]) == 1
assert s.peakIndexInMountainArray([0,1,2,3,4,5,4,3,2,1]) == 5
assert s.peakIndexInMountainArray([0,1,2,3,100,4,3,2,1]) == 4
assert s.peakIndexInMountainArray([0,5,4,3,2,1,0]) == 1
assert s.peakIndexInMountainArray([0,1,2,3,4,5,0]) == 5
assert s.peakIndexInMountainArray([0,1,2,0]) == 2
assert s.peakIndexInMountainArray([0,2,1,0]) == 1

# 10 minutes