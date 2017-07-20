class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        conditions...
            1. extend range from previous
            2. start again with height of current i
        keep track of the largest area so far?

        Sounds like a dynamic programming problem

        if so... what's the recurrence relation?
        """

        n = len(heights)
        areas = [-1 for i in range(n)] # max seen so far
        bestHeights = [-1 for i in range(n)]

        areas[0] = heights[0]
        bestHeights[0] = heights[0]

        for i in range(n):
            areas[i] = max(areas[i-1] + bestHeights[i-1],
                           heights[i])

            if areas[i-1] + bestHeights[i-1] > heights[i]:
                bestHeights[i] = bestHeights[i-1]
            else:
                bestHeights[i] = heights[i]

        print "    heights:",
        for j in heights:
            print '{:3d}'.format(j),
        print

        print "bestHeights:",
        for j in bestHeights:
            print '{: 3d}'.format(j),
        print

        print "      areas:",
        for j in areas:
            print '{: 3d}'.format(j),
        print




s = Solution()
assert 10 == s.largestRectangleArea([2,1,5,6,2,3])
assert 16 == s.largestRectangleArea([5,8,11])
