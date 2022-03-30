from typing import List
from colorama import init, Fore, Style
init()

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for row in matrix:
            lst.extend(row)

        lo = 0
        hi = len(lst) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target < lst[mid]:
                hi = mid - 1
            elif target > lst[mid]:
                lo = mid + 1
            else:
                return True

        return False

    def searchMatrixWithoutList(self, matrix: List[List[int]], target: int):
        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1
        # print("==================")
        # print("rows", rows, "cols", cols)
        while lo <= hi:
            mid = (lo + hi) // 2
            y = mid // cols
            x = mid % cols
            # print(lo, hi, mid, "\t", "y", y, "x", x, "value", matrix[y][x])
            # print(highlightXY(matrix, y, x))

            if target < matrix[y][x]:
                hi = mid - 1
            elif target > matrix[y][x]:
                lo = mid + 1
            else:
                return True

        return False

    def searchMatrixAgain(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // n
            c = mid % n

            if target < matrix[r][c]:
                hi = mid - 1
            elif target > matrix[r][c]:
                lo = mid + 1
            else:
                return True

        return False

def highlightXY(matrix: List[List[int]], y: int, x: int) -> str:
    s = ""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            formatted = "{:8}".format(matrix[i][j])
            if i == y and j == x:
                s += Fore.RED + formatted + Style.RESET_ALL
            else:
                s += formatted
        s += "\n"
    return s

s = Solution()

matrix = [[1,   3,  5,  7],
          [10,  11, 16, 20],
          [23,  30, 34, 50]]

for row in matrix:
    for value in row:
        assert s.searchMatrixWithoutList(matrix, value) == True
        assert s.searchMatrixAgain(matrix, value) == True

for value in [0,2,4,6,9,13,18,21,25,32,41,61]:
    assert s.searchMatrixWithoutList(matrix, value) == False
    assert s.searchMatrixAgain(matrix, value) == False

import random
random.seed(0)
m = 20
n = 20
lst = sorted(random.sample(range(m*m*n*n),m*n))
m2 = []
for k in range(0, len(lst), n):
    m2.append(lst[k:k+n])

for value in lst:
    assert s.searchMatrixWithoutList(m2, value) == True
    assert s.searchMatrixAgain(m2, value) == True

# check between values in lst for values that don't exist
assert s.searchMatrixWithoutList(m2, lst[0] - 1) == False
assert s.searchMatrixWithoutList(m2, lst[~0] + 1) == False
assert s.searchMatrixAgain(m2, lst[0] - 1) == False
assert s.searchMatrixAgain(m2, lst[~0] + 1) == False
for l, r in zip(lst, lst[1:]):
    if l+1 < r:
        for value in random.sample(range(l+1, r), 1):
            assert s.searchMatrixWithoutList(m2, value) == False
            assert s.searchMatrixAgain(m2, value) == False
