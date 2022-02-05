from typing import List

class Solution:
    def find(self, x: int) -> int:
        if self.graph[x] != x:
            rootparent = self.find(self.graph[x])
            self.graph[x] = rootparent

        return self.graph[x]

    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            self.graph[rootx] = rooty
            self.changes += 1

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        self.changes = 0
        self.graph = [i for i in range(n)]

        for (timestamp, x, y) in logs:
            self.union(x, y)
            if self.changes == n - 1:
                return timestamp

        return -1

s = Solution()

assert s.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6) == 20190301
assert s.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4) == 3
assert s.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]][::-1], 4) == 3
assert s.earliestAcq([[1,3,2],[0,2,0]], 4) == -1
