class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # so the naive solution would be O(n^2)
        # for each 0<=i<n, j>=i
        #   keep track of the max diff of prices[i] - prices[i]

        # what's a solution that's in O(n)?

        # recurrence relation...
        # maxDiff(A[N]) = max(maxDiff(A[n-1]), (A[N] - min))
        # maxDiff(A[0]) = 0

        if not prices:
            return 0

        lowest = prices[0]
        highest = 0
        diffs = [0 for i in prices]
        # [ 0, .... ]

        i = 1
        while i < len(prices):
            if prices[i] < lowest:
                lowest = prices[i]

            diff = prices[i] - lowest
            diffs[i] = max(diffs[i-1], diff)

            i += 1

        return diffs[-1]


# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# Input: [7, 6, 4, 3, 1]
# Output: 0

s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
print s.maxProfit([7, 6, 4, 3, 1])
