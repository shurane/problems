from colorama import init, Fore, Style
init()

class Solution:
    def searchMatrix(self, matrix, target):
        
        lst = []
        for row in matrix:
            lst.extend(row)
        lst = sorted(lst)
        
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

    def searchMatrixWithoutList(self, matrix, target):
        if not matrix:
            return False

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
            # print(printMatrix(matrix, y, x))

            if target < matrix[y][x]:
                hi = mid - 1
            elif target > matrix[y][x]:
                lo = mid + 1
            else:
                return True
        
        return False

def printMatrix(matrix, y, x, color=Fore.RED):
    s = ""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            formatted = "{:4}".format(matrix[i][j])
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


import numpy as np
np.random.seed(0)
matrix2 = np.random.randint(999, size=49)
matrix2.sort()
matrix2.shape = (7,7)
matrix2 = matrix2.tolist()


s = Solution()
assert s.searchMatrixWithoutList([], 1) == False
assert s.searchMatrixWithoutList(matrix, 13) == False
assert s.searchMatrixWithoutList(matrix, 1) == True
assert s.searchMatrixWithoutList(matrix, 11) == True
assert s.searchMatrixWithoutList(matrix, 50) == True
assert s.searchMatrixWithoutList(matrix, 20) == True
assert s.searchMatrixWithoutList(matrix, 21) == False
assert s.searchMatrixWithoutList(matrix2, 21) == False
        
# 15 minutes
