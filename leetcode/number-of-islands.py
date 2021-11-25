from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(y: int, x: int):
            stack = [(y, x)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = None
                for ni, nj in [(1,0), (-1,0), (0,1),(0,-1)]:
                    if 0 <= i + ni < m and 0 <= j + nj < n and grid[ni + i][nj + j] == "1":
                        stack.append((i + ni, j  + nj))

        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    helper(i, j)
        return count

# # This is a different approach. It would be cool if it worked with a single pass through the array.
# # But it probably doesn't work. Discussed with Dorian on 2021/11/18
#     def numIslandsDorian(self, grid: List[List[str]]) -> int:
#         count = 1
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     if j > 0 and grid[i][j-1] != 0 or i > 0 and grid[i-1][j] != 0:
#                         # don't mark as new island because we're connected to the left or above
#                         # print(f"{i}, {j} is connected to existing island")
#                         # grid[i][j] = count
#                         pass
#                     else:
#                         grid[i][j] = count
#                         count += 1
#                 # elif grid[i][j] == "0":
#                 else:
#                     grid[i][j] = 0

#         # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
#         print(count)
#         # print()
#         print(*(" ".join([c(i) for i in row]) for row in grid), sep="\n")


# # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# BLACK   = "\u001b[30m"
# RED     = "\u001b[31m"
# B_RED   = "\u001b[91m"
# GREEN   = "\u001b[32m"
# YELLOW  = "\u001b[33m"
# BLUE    = "\u001b[34m"
# MAGENTA = "\u001b[35m"
# CYAN    = "\u001b[36m"
# WHITE   = "\u001b[37m"
# RESET   = "\u001b[0m"

# def c(i):
#     if int(i) == 0: return f"{int(i):2}"
#     elif int(i) == 1: return f"{RED}{int(i):2}{RESET}"
#     else: return f"{BLUE}{i:2}{RESET}"

def to_s(grid: List[List[int]]) -> List[List[str]]:
    return [[str(x) for x in row] for row in grid]

islands1 = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [ 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [ 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [ 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [ 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

islands2 = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [ 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


islands3 = [[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]


islands4 = [[ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            [ 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [ 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [ 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [ 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [ 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            [ 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0]]

# # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
# print(*(" ".join([c(i) for i in row]) for row in islands4), sep="\n")

s = Solution()
assert s.numIslands([["1"]]) == 1
assert s.numIslands([["1", "0"], ["0", "1"]]) == 2
assert s.numIslands([["1", "1"], ["0", "1"]]) == 1
assert s.numIslands([["1", "0"], ["1", "1"]]) == 1
assert s.numIslands(to_s(islands1)) == 1
assert s.numIslands(to_s(islands2)) == 4
assert s.numIslands(to_s(islands3)) == 50
assert s.numIslands(to_s(islands4)) == 2
