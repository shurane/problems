from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # reversed(range(len(triangle) - 1)) is more readable
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

    # this solution is similar to `longest-increasing-path-in-a-matrix`
    # I guess this is kind of like a DP problem. There are two approaches... top down (minimumTotal2) and bottom up (minimumTotal)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        cache = dict()
        return self.helper(triangle, 0, 0, cache)


    def helper(self, triangle, i, j, cache) -> int:
        if (i, j) in cache:
            return cache[(i, j)]
        elif i >= len(triangle) or j >= len(triangle[i]):
            return 0

        minValue = triangle[i][j] + min(self.helper(triangle, i + 1, j, cache), self.helper(triangle, i + 1, j + 1, cache))
        cache[(i, j)] = minValue
        return minValue

s = Solution()

assert s.minimumTotal([[-10]]) == -10
assert s.minimumTotal([[1],[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1]]) == 5
assert s.minimumTotal([[1],[1,9],[1,9,9],[1,9,9,9],[1,9,9,9,9]]) == 5
assert s.minimumTotal([[1],[9,1],[9,9,1],[9,9,9,1],[9,9,9,9,1]]) == 5
assert s.minimumTotal([[1],[9,1],[9,9,1],[9,9,1,9],[9,9,1,9,9]]) == 5
assert s.minimumTotal([[1],[9,1],[9,9,1],[9,9,1,9],[9,9,1,9,9],[9,9,1,9,9,9],[19,9,1,9,9,9,9]]) == 7
assert s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11