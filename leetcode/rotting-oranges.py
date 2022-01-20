from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        minutes = 0
        rottenQ = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rottenQ.append((i, j))

        # # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print("matrix")
        # print(*(" ".join([str(c) for c in row]) for row in grid), sep="\n")

        while rottenQ and fresh > 0:
            nextRottenQ = []
            # print(f"minutes:{minutes}, fresh:{fresh}, rottenQ:{rottenQ}")
            for i, j in rottenQ:
                for ni, nj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= i + ni < m and 0 <= j + nj < n and grid[i+ni][j+nj] == 1:
                        nextRottenQ.append((i + ni, j + nj))
                        grid[i+ni][j+nj] = 2
                        fresh -= 1
            if nextRottenQ:
                minutes += 1
            rottenQ = nextRottenQ

        if fresh == 0:
            return minutes
        return -1

s = Solution()

assert s.orangesRotting([[0]]) == 0
assert s.orangesRotting([[2]]) == 0
assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2
assert s.orangesRotting([[2,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1]]) == 12
assert s.orangesRotting([[0,2]]) == 0