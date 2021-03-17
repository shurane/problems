from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # definitely a DP type problem. I am weak at these...
        # based on https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108871/2-solutions-2-states-DP-solutions-clear-explanation!
        # explanation of all variation problems of buy/sell stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        buy = [0 for elem in prices]
        sell = [0 for elem in prices]
        buy[0] = - prices[0] - fee

        i = 1
        while i < len(prices):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i] - fee) # hold onto the current purchase, or sell and buy at current price
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i]) # hold no stock, or buy from the previous price and sell at current
            i += 1

        # print(prices)
        # print(buy)
        # print(sell)

        return sell[-1]

s = Solution()
assert s.maxProfit([1], 0) == 0
assert s.maxProfit([1,2,3,4], 2) == 1
assert s.maxProfit([1,1,1,1,1,1], 0) == 0
assert s.maxProfit([1,2,3,4,5], 0) == 4
assert s.maxProfit([10,10,10,10,0,10], 5) == 5
assert s.maxProfit([10,10,0,10,0,10], 5) == 10
assert s.maxProfit([1,3,2,8,4,9], 2) == 8
assert s.maxProfit([1,3,7,5,10,3], 3) == 6