from typing import List
from unittest import TestCase
tc = TestCase()

PACIFIC = 1
ATLANTIC = 2
BOTH = PACIFIC | ATLANTIC

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(q: List[List[int]], ocean: int):
            # mark the initial coordinates with ocean
            for y, x in q:
                visited[y][x] |= ocean

            while q:
                nextq = []
                for y, x in q:
                    if visited[y][x] == BOTH:
                        both.append([y,x])
                    for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                        yi = y + i
                        xj = j + x
                        # check the new cell is within bounds, isn't marked with 'ocean', and its height is greater
                        if (0 <= yi < m and 0 <= xj < n
                            and visited[yi][xj] & ocean != ocean
                            and heights[yi][xj] >= heights[y][x]):
                            visited[yi][xj] |= ocean
                            nextq.append([yi, xj])
                q = nextq

        m = len(heights)
        n = len(heights[0])
        visited = [[0 for __ in range(n)] for _ in range(m)]
        both = []

        # prepopulate with pacific tiles: topleft corner, top row, left column
        q = [[0, 0]]
        for c in range(1, n):
            q.append([0, c])
        for c in range(1, m):
            q.append([c, 0])

        helper(q, PACIFIC)

        # prepopulate with atlantic tiles: bottomright corner, bottom row, right column
        q = [[m - 1, n - 1]]
        for c in range(0, n - 1):
            q.append([m - 1, c])
        for c in range(0, m - 1):
            q.append([c, n - 1])

        helper(q, ATLANTIC)

        return both

s = Solution()

m1 = [[2,1],[1,2]]
tc.assertCountEqual(s.pacificAtlantic(m1), [[0,0],[0,1],[1,0],[1,1]])

m2 = [[1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]]
tc.assertCountEqual(s.pacificAtlantic(m2), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

# only 2 corners flow into both oceans
m3 = [[4,3,3,3,4],
      [3,2,2,2,3],
      [3,2,1,2,3],
      [3,2,2,2,3],
      [4,3,3,3,4]]
tc.assertCountEqual(s.pacificAtlantic(m3), [[0,4],[4,0]])

# flows everywhere
m4 = [[2,2,2],[2,2,2],[2,2,2]]
tc.assertCountEqual(s.pacificAtlantic(m4), [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])

m5 = [[2,3,2],[2,3,3],[2,2,2]]
tc.assertCountEqual(s.pacificAtlantic(m5), [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])

m6 = [[13], [4], [19], [10], [1], [11], [5], [17], [3], [10], [1], [0], [1], [4], [1], [3], [6], [13],
      [2], [16], [7], [6], [3], [1], [9], [9], [13], [10], [9], [10], [6], [2], [11], [17], [13], [0],
      [19], [7], [13], [3], [9], [2]]

assert len(s.pacificAtlantic(m6)) == len(m6)
