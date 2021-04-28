from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        counts = [[0 for i in row] for row in obstacleGrid]
        if obstacleGrid[0][0] != 1: counts[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                counts[i][0] = counts[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                counts[0][j] = counts[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    counts[i][j] = counts[i-1][j] + counts[i][j-1]

        # print("counts")
        # print(*(" ".join([f"{i:2}" for i in row]) for row in counts), sep="\n")

        return counts[m-1][n-1]

s = Solution()

assert s.uniquePathsWithObstacles([[0,0],[0,0]]) == 2
assert s.uniquePathsWithObstacles([[1]]) == 0
assert s.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]) == 6

assert s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
assert s.uniquePathsWithObstacles([[0,1],[0,0]]) == 1