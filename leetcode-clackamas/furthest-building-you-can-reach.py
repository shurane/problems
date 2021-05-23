from typing import List
from heapq import heappop, heappush

class Solution:
    def furthestBuilding2(self, heights: List[int], bricks: int, ladders: int) -> int:
        # from https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918374/Basic-Priority-Queue-Single-Pass-or-Code-with-Comments-or-Corner-Cases
        used = 0
        s = []

        for i in range(len(heights) - 1):
            if heights[i+1] < heights[i]:
                continue

            diff = heights[i+1] - heights[i]

            if used + diff <= bricks:
                used += diff
                heappush(s, -diff)
            elif ladders > 0:
                if s and -s[0] > diff:
                    # print("using a ladder and removing", -s[0], "bricks")
                    used -= -s[0] - diff
                    heappop(s)
                    heappush(s, -diff)
                ladders -= 1
            else:
                return i

            # print(f"{i:2}, {heights[i]:3} to {heights[i+1]:3}, bricks used: {used-diff:3} + {diff:3} to {used:3}, ladders left: {ladders:2}, heap:{s}")

        return len(heights) - 1

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # non working DP solution, bottom up
        n = len(heights)
        bl = [[None for i in range(n)] for j in range(n)] #bricks on y-axis, ladders on x-axis

        bl[0][0] = None
        bl[1][0] = [bricks, ladders]
        bl[0][1] = [bricks, ladders]

        # bottom up approach
        for i in range(2, n):
            diff = heights[i] - heights[i-1]

            # bricks
            if diff <= 0:
                bl[i][0] = bl[i-1][0]
            elif bl[i-1][0] != None and diff <= bl[i-1][0][0]:
                temp = bl[i-1][0]
                temp[0] -= diff
                bl[i][0] = temp[:]
            else:
                # temp = bl[i-1][0]
                # temp[0] = -1
                bl[i][0] = None

            # ladders
            if diff <= 0:
                bl[0][i] = bl[0][i-1]
            elif bl[0][i-1] != None and bl[0][i-1][1] > 0:
                temp = bl[0][i-1]
                temp[1] -= 1
                bl[0][i] = temp[:]
            else:
                # temp = bl[0][i-1]
                # temp[1] = -1
                bl[0][i-1] = None

        # going down uses bricks. Going right uses a ladder. What does going diagonally mean? both bricks and ladder?
        for i in range(1, n - 1):
            diff = heights[i] - heights[i-1]
            reachable = diff <= 0
            useLadder = bl[i][i-1] != None and bl[i][i-1][1] > 0
            useBricks = bl[i-1][i] != None and diff <= bl[i-1][i][0]
            if reachable or useLadder or useBricks:
                bl[i][i] = True
            else:
                bl[i][i] = False

            if useBricks:
                temp = bl[i-1][i]
                temp[0] -= diff
                bl[i+1][i] = temp
            else:
                bl[i+1][i] = None

            if useLadder:
                temp = bl[i][i-1]
                temp[1] -= 1
                bl[i][i+1] = temp[:]
            else:
                bl[i][i+1] = None

        # # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print(f"{Fore.YELLOW}bl{Fore.RESET}")
        # print(*(" ".join([f"{str(i).ljust(6)}" for i in row]) for row in bl), sep="\n")

s = Solution()

assert s.furthestBuilding([10,9,8,7,6,5,4,3,2,1], 0, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 0, 5) == 5
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 10, 0) == 9
assert s.furthestBuilding([1,4,9,16,25,36,49,64,81,100], 99, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 9, 0) == 9
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 5, 0) == 5
assert s.furthestBuilding([1,2,3,4,5,6,7,8,9,10], 0, 10) == 9

assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 0, 10) == 9
assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 10, 0) == 5
assert s.furthestBuilding([2,4,6,8,10,12,14,16,18,20], 10, 5) == 9

assert s.furthestBuilding([1,51, 101], 0, 2) == 2
assert s.furthestBuilding([1,51, 101], 50, 1) == 2
assert s.furthestBuilding([1,51, 101], 100, 0) == 2
assert s.furthestBuilding([1,51, 101], 50, 0) == 1
assert s.furthestBuilding([1,51, 101], 0, 1) == 1
assert s.furthestBuilding([1,51, 101], 49, 1) == 1

assert s.furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4
assert s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7
assert s.furthestBuilding([14,3,19,3], 17, 0) == 3