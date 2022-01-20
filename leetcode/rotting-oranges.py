from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        minutes = -1
        rottenQ = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rottenQ.append((i, j))

        while rottenQ:
            minutes += 1
            nextRottenQ = []
            for i, j in rottenQ:
                for ni, nj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= i + ni < m and 0 <= j + nj < n and grid[i+ni][j+nj] == 1:
                        nextRottenQ.append((i + ni, j + nj))
                        grid[i+ni][j+nj] = 2
                        fresh -= 1
            rottenQ = nextRottenQ

        if fresh == 0:
            return max(minutes, 0)
        return -1

s = Solution()

assert s.orangesRotting([[0]]) == 0
assert s.orangesRotting([[2]]) == 0
assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2
assert s.orangesRotting([[2,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1]]) == 12
assert s.orangesRotting([[0,2]]) == 0