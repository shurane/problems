from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.prefixSum = [[0 for _ in row] for row in matrix]
        self.prefixSum[0][0] = matrix[0][0]
        for i in range(1, self.rows):
            self.prefixSum[i][0] = matrix[i][0] + self.prefixSum[i-1][0]

        for j in range(1, self.cols):
            self.prefixSum[0][j] = matrix[0][j] + self.prefixSum[0][j-1]

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + self.prefixSum[i][j-1] - self.prefixSum[i-1][j-1] + matrix[i][j]

        # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print(*(" ".join([f"{i:2}" for i in row]) for row in self.prefixSum), sep="\n")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # think of it as 4 quadrants, and we want the bottom right quadrant
        bottomright = self.prefixSum[row2][col2]

        topleft = 0
        topright = 0
        bottomleft = 0
        if row1 == 0 and col1 == 0:
            # we can just take bottomright as the answer because the range sum encompasses a square from 0,0
            pass
        elif row1 == 0:
            # only bottomleft exists
            bottomleft = self.prefixSum[row2][col1 - 1]
        elif col1 == 0:
            # only topright exists
            topright = self.prefixSum[row1 - 1][col2]
        else:
            topleft = self.prefixSum[row1 - 1][col1 - 1]
            bottomleft = self.prefixSum[row1 - 1][col2]
            topright = self.prefixSum[row2][col1 - 1]

        ans = bottomright - bottomleft - topright + topleft

        # print(f"topleft: {topleft:3}, topright: {topright:3}, bottomleft: {bottomleft:3}, bottomright: {bottomright:3}, ans: {ans:3}")

        return ans

s = NumMatrix([[1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1]])

assert s.sumRegion(0, 0, 0, 0) == 1
assert s.sumRegion(1, 1, 1, 1) == 1
assert s.sumRegion(2, 2, 2, 2) == 1
assert s.sumRegion(3, 3, 3, 3) == 1
assert s.sumRegion(4, 4, 4, 4) == 1

assert s.sumRegion(0, 0, 1, 1) == 4
assert s.sumRegion(1, 1, 2, 2) == 4
assert s.sumRegion(2, 2, 3, 3) == 4
assert s.sumRegion(3, 3, 4, 4) == 4

assert s.sumRegion(2, 1, 3, 3) == 6

assert s.sumRegion(0, 0, 2, 2) == 9
assert s.sumRegion(1, 1, 3, 3) == 9
assert s.sumRegion(2, 2, 4, 4) == 9

assert s.sumRegion(0, 0, 3, 3) == 16
assert s.sumRegion(1, 1, 4, 4) == 16

assert s.sumRegion(0, 0, 4, 4) == 25

t = NumMatrix([[3, 0, 1, 4, 2],
               [5, 6, 3, 2, 1],
               [1, 2, 0, 1, 5],
               [4, 1, 0, 1, 7],
               [1, 0, 3, 0, 5]])

assert t.sumRegion(2, 1, 4, 3) == 8
assert t.sumRegion(1, 1, 2, 2) == 11
assert t.sumRegion(1, 2, 2, 4) == 12