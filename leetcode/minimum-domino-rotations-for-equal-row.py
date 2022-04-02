from typing import List

class Solution:
    # https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC%2B%2BPython-Different-Ideas
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        countA = [0] * 7
        countB = [0] * 7
        same   = [0] * 7

        for i in range(n):
            countA[tops[i]] += 1
            countB[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same[tops[i]] += 1

        for i in range(1,7):
            if countA[i] + countB[i] - same[i] == n:
                return n - max(countA[i], countB[i])
        return -1

s = Solution()

assert s.minDominoRotations([1,1], [2,2]) == 0
assert s.minDominoRotations([1,2], [2,1]) == 1
assert s.minDominoRotations([1,2], [2,2]) == 0
assert s.minDominoRotations([2,1], [2,2]) == 0

assert s.minDominoRotations([1,2,3], [4,5,6]) == -1
assert s.minDominoRotations([1,2,1], [4,1,6]) == 1
assert s.minDominoRotations([1,2,2], [2,2,1]) == 1

assert s.minDominoRotations([1,2,1], [2,3,4]) == -1

assert s.minDominoRotations([1,2,1,3,1,3,1], [2,1,2,1,2,1,2]) == 3

assert s.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]) == 2
assert s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]) == -1

assert s.minDominoRotations([2,1,1,3,2,1,2,2,1], [3,2,3,1,3,2,3,3,2]) == -1

t1 = [1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,1,1,2,2,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,2,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,1,2,1,1,2,1,2,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,2,1,2,1,2,1,1,2,2,2,1,2,2,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,2,2,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,2,2,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,1,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,2,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,2,1,2,1,1,1,1,2,2,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,2,2,1,2,1,2,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,2,1,2,2,1,2,1,1,1,1,1,2,1,2,2,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,2,1,2,1,1,1,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,2,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,2,2,1,2,2,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,2,1,2,1,1,2,1,2,2,1,2,2,1,2,2,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,2,1,1,1,1,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,2,1,1,2,1,2,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,1,2,1,2,2,1,1,1,2,2,1,2,1,1,2,2,1,1,2,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,2,2,2,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,2,1,2,1,1,2,2,1,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,2,1,2,2,1,1,2,2,1,1,2,2,1,1,1,2,2,1,2,1,2,1,1,1,1,2,1,2,2,2,2,2,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,2,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,2,2,1,1,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,2,1,2,2,1,1,1,1,2,1,1,1,2,1,2,2,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,2,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,2,1,1,1,2,2,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2,2,1,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,1,2,2,1,2,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,2,1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,2,2,2,2,1,2,1,2,2,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,2,2,1,2,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,2,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2,2,1,2,2,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,2,1,1,2,2,1,2,2,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,2,2,1,1,2,1,1,1,1,1,2,2,1,1,2,2,2,1,1,2,1,2,1,1,2,2,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1]
b1 = [1,2,1,1,2,1,1,1,1,1,1,2,2,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,2,1,2,2,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,2,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,2,2,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,2,1,2,1,1,1,1,1,1,1,2,2,1,2,2,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,2,1,2,1,1,2,2,1,2,1,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,2,2,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,1,2,2,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,2,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,2,1,2,1,1,2,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,2,2,2,1,1,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,2,1,1,2,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,2,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,2,2,1,1,1,2,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,2,2,2,2,1,1,2,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,1,2,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,2,2,1,1,2,2,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,1,1,2,1,2,1,2,2,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,2,1,1,2,1,1,2,1,1,1,1,2,1,2,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,2,2,1,1,2,1,1,1,1,2,2,1,2,1,1,1,2,1,1,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,2,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,1,2,2,1,2,1,1,2,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,2,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,2,1,2,1,1,2,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,2,2,1,1,2,2,1,1,1,2,1,1,1,2,1,2,2]
assert s.minDominoRotations(t1, b1) == 608