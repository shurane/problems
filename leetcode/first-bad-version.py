# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n

        while lo <= hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        if not isBadVersion(mid):
            return mid + 1
        else:
            return mid