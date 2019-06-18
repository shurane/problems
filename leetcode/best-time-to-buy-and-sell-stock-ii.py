from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        lowest = 0
        i = 1

        while i < len(prices):
            if prices[i] < prices[i-1]:
                total += prices[i-1] - prices[lowest]
                lowest = i
            # we're at the end, we should add whatever is left
            elif i == len(prices) - 1:
                value = prices[i] - prices[lowest]
                if value > 0:
                    total += value

            i += 1

        return total

    def maxProfit2(self, prices: List[int]) -> int:
        # I believe this works, but not sure until it's tested
        # see https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39402/Is-this-question-a-joke/221879

        # from discussions in https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39402/Is-this-question-a-joke
        # see peak-valley pattern
        # 416486188 describes it as "the sum of the diff of prices of [--longest--] ascending arrays"
        if len(prices) <= 1:
            return 0

        total = 0
        lowest = 0
        i = 1

        while i < len(prices):
            if prices[i] < prices[i-1]:
                total += prices[i-1] - prices[lowest]
                lowest = i

            i += 1

        total += prices[-1] - prices[lowest]
        return total

s = Solution()

assert s.maxProfit([]) == 0
assert s.maxProfit([1000]) == 0
assert s.maxProfit([7,1,5,3,6,4]) == 7
assert s.maxProfit([1,2,3,4,5]) == 4
assert s.maxProfit([7,6,4,3,1]) == 0
assert s.maxProfit([7,1,5,3,6,4,1,2,3,4,5]) == 11