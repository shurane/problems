class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # There's probably a math-y sort of approach to this

        # here's a simple approach using DP, since m<=100 and n<=100
        # grid[m, n] = grid[m-1][n] + grid[m][n-1]
        # grid[0, j] = 1
        # grid[i, 0] = 1
        # grid[0, 0] = 1

        grid = [ [0 for i in xrange(n)] for j in xrange(m) ]

        grid[0][0] = 1

        for i in xrange(1, m):
            grid[i][0] = 1

        for j in xrange(1, n):
            grid[0][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]

s = Solution()
print s.uniquePaths(1,1)
print s.uniquePaths(1,2)
print s.uniquePaths(2,1)
print s.uniquePaths(2,2)
print s.uniquePaths(3,3)
print s.uniquePaths(4,4)
print s.uniquePaths(5,5)
print s.uniquePaths(6,6)
print s.uniquePaths(1, 100)
print s.uniquePaths(100, 1)
print s.uniquePaths(100, 100)
