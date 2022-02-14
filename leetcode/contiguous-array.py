from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        p0 = [0] * (n+1)
        p1 = [0] * (n+1)

        best = 0

        # n^2 solution
        for i in range(n):
            if nums[i] == 0:
                p0[i+1] = p0[i] + 1
                p1[i+1] = p1[i]
            else:
                p0[i+1] = p0[i]
                p1[i+1] = p1[i] + 1

            for j in range(0, i+1):
                count0 = p0[i+1] - p0[j]
                count1 = p1[i+1] - p1[j]
                if count0 == count1 and i + 1 - j > best:
                    best = i + 1 - j

        # print("nums   ", "".join([f"{i: 3}" for i in nums]))
        # print("  p0", "".join([f"{i: 3}" for i in p0]))
        # print("  p1", "".join([f"{i: 3}" for i in p1]))

        # print("best", best)
        # print()
        return best

    # https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
    # can either do i + 1, or change yAxisIntercepts to {0: -1}
    # It's a little confusing why there's an offset.
    # Looks like [0,0,1,1] would match at index 0 to index 3, but the run is length 4, i.e. (3 + 1) - 0 == 4
    #        for [1,1,0,0,1], it would be index 1 to index 4, run is length 4, so (4 + 1) - 1 == 4
    # more explanation at https://leetcode.com/problems/contiguous-array/discuss/99646/Easy-Java-O(n)-Solution-PreSum-+-HashMap/561999
    def findMaxLengthFaster(self, nums: List[int]) -> int:
        count = 0
        best = 0
        yAxisIntercepts = {0: 0}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in yAxisIntercepts:
                best = max(best, i + 1 - yAxisIntercepts[count])
            else:
                yAxisIntercepts[count] = i + 1

        return best

s = Solution()

assert s.findMaxLengthFaster([1]) == 0
assert s.findMaxLengthFaster([0]) == 0
assert s.findMaxLengthFaster([0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
assert s.findMaxLengthFaster([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == 4
assert s.findMaxLengthFaster([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
assert s.findMaxLengthFaster([0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 30
assert s.findMaxLengthFaster([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 30
assert s.findMaxLengthFaster([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 30