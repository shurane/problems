class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        minPrice = prices[0]
        profit = 0

        i = 1
        while i < len(prices):
            if prices[i] < minPrice:
                minPrice = prices[i]

            potentialProfit = prices[i] - minPrice
            if potentialProfit > profit:
                profit = potentialProfit
            i += 1

        return profit