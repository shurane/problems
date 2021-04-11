from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        longest = 0
        # had some help from https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78308/15ms-Concise-Java-Solution for figuring out the cache
        cache: List[List[int]] = [[0 for j in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                current = helper(matrix, m, n, row, col, cache)
                if current > longest:
                    # can reconstruct the path by backtracking the (row, col) values in cache
                    longest = current

        # print("cache", cache)
        # print("longest", longest)
        return longest

def helper(matrix: List[List[int]], m: int, n: int, r: int, c: int, cache: List[List[int]]) -> int:
    if cache[r][c] != 0: return cache[r][c]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    longest = 0
    for i, j in directions:
        rr = r + i
        cc = c + j
        if 0 <= rr < m and 0 <= cc < n and matrix[rr][cc] > matrix[r][c]:
            # print("from", r, c, "->", rr, cc)
            result = helper(matrix, m, n, rr, cc, cache)

            if result > longest:
                longest = result
    cache[r][c] = 1 + longest
    return cache[r][c]

s = Solution()

assert s.longestIncreasingPath([[1]]) == 1
assert s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
assert s.longestIncreasingPath([[1,2,3],[6,5,4],[7,8,9]]) == 9
assert s.longestIncreasingPath([[9,8,7],[4,5,6],[3,2,1]]) == 9
assert s.longestIncreasingPath([[7,8,9],[4,5,6],[3,2,1]]) == 7

medMatrix = [
    [0,1,2,3,4],
    [9,8,7,6,5],
    [10,11,12,13,14],
    [19,18,17,16,15],
    [20,21,22,23,24],
    [29,28,27,26,25],
    [30,31,32,33,34],
    [39,38,37,36,35],
    [40,41,42,43,44],
    [49,48,47,46,45]
]

bigMatrix = [
    [0,1,2,3,4,5,6,7,8,9],
    [19,18,17,16,15,14,13,12,11,10],
    [20,21,22,23,24,25,26,27,28,29],
    [39,38,37,36,35,34,33,32,31,30],
    [40,41,42,43,44,45,46,47,48,49],
    [59,58,57,56,55,54,53,52,51,50],
    [60,61,62,63,64,65,66,67,68,69],
    [79,78,77,76,75,74,73,72,71,70],
    [80,81,82,83,84,85,86,87,88,89],
    [99,98,97,96,95,94,93,92,91,90],
    [100,101,102,103,104,105,106,107,108,109],
    [119,118,117,116,115,114,113,112,111,110],
    [120,121,122,123,124,125,126,127,128,129],
    [139,138,137,136,135,134,133,132,131,130],
    [0,0,0,0,0,0,0,0,0,0]]

assert s.longestIncreasingPath(medMatrix) == 50
assert s.longestIncreasingPath(bigMatrix) == 140