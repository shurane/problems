from typing import List
# from colorama import init, Fore
# init()

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print(f"{Fore.YELLOW}matrix before{Fore.RESET}")
        # print(*(" ".join([f"{i:2}" for i in row]) for row in matrix), sep="\n")

        for begin in range(n // 2):
            # print(f"{Fore.BLUE}layer {begin}{Fore.RESET}")
            cellsInLayer= n - begin * 2
            end = begin + cellsInLayer - 1
            # print(f"begin: {begin}, end: {end}, cellsInLayer: {cellsInLayer}")

            for c in range(cellsInLayer - 1):
                # print(matrix[begin][begin+c],
                #       matrix[begin+c][end],
                #       matrix[end][end-c],
                #       matrix[end-c][begin])
                temp = matrix[begin][begin + c]
                matrix[begin][begin + c] = matrix[end - c][begin]
                matrix[end - c][begin] = matrix[end][end - c]
                matrix[end][end - c] = matrix[begin + c][end]
                matrix[begin + c][end] = temp

            # # iterate top side from left to right
            # for j in range(begin, end):
            #     print("   top", matrix[begin][j])

            # # iterate right side from top to bottom
            # for j in range(begin, end):
            #     print(" right", matrix[j][end])

            # # iterate bottom side, from right to left
            # for j in range(end, begin, -1):
            #     print("bottom", matrix[end][j])

            # # iterate left side, from bottom to top
            # for j in range(end, begin, -1):
            #     print("  left", matrix[j][begin])

        # print(f"{Fore.YELLOW}matrix after{Fore.RESET}")
        # print(*(" ".join([f"{i:2}" for i in row]) for row in matrix), sep="\n")

s = Solution()

m1 = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(m1)
assert m1 == [[7,4,1],[8,5,2],[9,6,3]]

m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(m2)
assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

m3 = [[1]]
s.rotate(m3)
assert m3 == [[1]]

m4 = [[1,2],[3,4]]
s.rotate(m4)
assert m4 == [[3,1],[4,2]]

# m5 = [[ 1, 2, 3, 4, 5],
#       [ 6, 7, 8, 9,10],
#       [11,12,13,14,15],
#       [16,17,18,19,20],
#       [21,22,23,24,25]]
# s.rotate(m5)

# m6 = [[ 1, 2, 3, 4, 5],
#       [16,17,18,19, 6],
#       [15,24,25,20, 7],
#       [14,23,22,21, 8],
#       [13,12,11,10, 9]]
# s.rotate(m6)