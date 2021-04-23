from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = dict()
        breaks = 0
        for row in wall:
            count = 0
            for cell in row[:-1]:
                count += cell

                if count in h:
                    h[count] += 1
                else:
                    h[count] = 1

                if h[count] > breaks:
                    breaks = h[count]

        # print(len(wall), breaks, len(wall) - breaks, h)

        return len(wall) - breaks

s = Solution()

s.leastBricks([[1,1,1],
               [1,1,1],
               [1,1,1],
               [1,1,1],
               [1,1,1],
               [1,1,1]]) == 0
# s.leastBricks([[2,1],
#                [1,2],
#                [1,1,1],
#                [1,1,1],
#                [1,1,1],
#                [1,1,1]]) == 1
# s.leastBricks([[2,1],
#                [1,2],
#                [2,1],
#                [1,2],
#                [1,1,1],
#                [1,1,1]]) == 2

s.leastBricks([[1,2,2,1],
               [3,1,2],
               [1,3,2],
               [2,4],
               [3,1,2],
               [1,3,1,1]]) == 2
s.leastBricks([[1],[1],[1]]) == 3