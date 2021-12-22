from typing import List

class Solution:
    # see https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
    # the DP solution is very intriguing, and really reminds me of what Dorian tried to do for Number of Islands and Pacific Atlantic Water Flow
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[-1 for __ in range(n)] for _ in range(m)]
        stack = []
        nextStack = []

        def checkAdjacent(i: int, j: int, distance: int) -> None:
            for y, x in [(-1,0),(1,0),(0,-1),(0,1)]:
                iy, jx = i+y, j+x
                # check if out of bounds or if iy, jx has been visited already
                if 0 <= iy < m and 0 <= jx < n and visited[iy][jx] == -1:
                    visited[iy][jx] = distance + 1
                    nextStack.append((iy, jx, distance + 1))

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = 0
                    stack.append((i, j, 0))

        while stack:
            nextStack = []
            for i, j, distance in stack:
                checkAdjacent(i, j, distance)
            stack = nextStack

        return visited

s = Solution()
assert s.updateMatrix([[0,1,1],[1,1,1],[1,1,1]]) == [[0,1,2],[1,2,3],[2,3,4]]
assert s.updateMatrix([[1,1,1],[1,0,1],[1,1,1]]) == [[2,1,2],[1,0,1],[2,1,2]]
assert s.updateMatrix([[0,1,0],[1,1,1],[0,1,0]]) == [[0,1,0],[1,2,1],[0,1,0]]

assert s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]