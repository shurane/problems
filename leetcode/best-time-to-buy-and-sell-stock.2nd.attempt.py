class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        # min_prices = [prices[0]] * len(prices)
        # bests = [0]
        best = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > best:
                best = prices[i] - min_price

            # bests.append(best)

        # print(min_prices)
        # print(profits)
        # print(bests)
        return best


s = Solution()
assert s.maxProfit([7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6,4,3,1]) == 0