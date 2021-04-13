from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # what I followed: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106948/C%2B%2B-Java-Clean-Code-4-liner
        # basically need to decide whether to add an increasing number or a decreasing number from 1 to k, and then have the rest as steadily increasing

        # IMO, a better, more pythonic way https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106965/Python-Straightforward-with-Explanation
        nums = []

        i = 1
        j = n
        while i <= j:
            if k > 1:
                if k % 2 != 0:
                    nums.append(i)
                    i += 1
                else:
                    nums.append(j)
                    j -= 1
                k -= 1
            else:
                nums.append(i)
                i += 1

        print(nums)
        return nums

    def constructArrayDiffs(self, n: int, k:int) -> List[int]:
        return len(diffs(self.constructArray(n, k)))

def diffs(array: List[int]) -> List[int]:
    d = []
    for i in range(len(array) - 1):
        d.append(abs(array[i] - array[i + 1]))
    return sorted(list(set(d)))

s = Solution()

assert s.constructArrayDiffs(3, 1) == 1
assert s.constructArrayDiffs(3, 2) == 2
assert s.constructArrayDiffs(10, 1) == 1
assert s.constructArrayDiffs(10, 2) == 2
assert s.constructArrayDiffs(10, 3) == 3
assert s.constructArrayDiffs(10, 4) == 4
assert s.constructArrayDiffs(10, 5) == 5
assert s.constructArrayDiffs(10, 6) == 6
assert s.constructArrayDiffs(10, 7) == 7
assert s.constructArrayDiffs(10, 8) == 8
assert s.constructArrayDiffs(10, 9) == 9
