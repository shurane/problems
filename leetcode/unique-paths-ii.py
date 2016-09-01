class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # same as unique paths, just check for obstacles

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [ [0 for i in xrange(n)] for j in xrange(m) ]

        if obstacleGrid[0][0] == 1:
            grid[0][0] = 0
        else:
            grid[0][0] = 1

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1 or grid[i-1][0] == 0:
                grid[i][0] = 0
            else:
                grid[i][0] = 1

        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1 or grid[0][j-1] == 0:
                grid[0][j] = 0
            else:
                grid[0][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        for row in grid:
            print row

        return grid[-1][-1]

s = Solution()
# print s.uniquePathsWithObstacles([[0]])
# print s.uniquePathsWithObstacles([[1]])
# print s.uniquePathsWithObstacles(
# [ [0,0,0],
  # [0,1,1],
  # [0,0,0] ]
# )
# print s.uniquePathsWithObstacles(
# [ [0,0,0],
  # [1,1,1],
  # [0,0,0] ]
# )
# print s.uniquePathsWithObstacles(
# [ [1,0,0],
  # [0,0,0],
  # [0,0,0] ]
# )
