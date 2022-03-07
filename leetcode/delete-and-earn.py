from typing import List

class Solution:
    def deleteAndEarnFirstAttempt(self, nums: List[int]) -> int:
        points = dict()
        for num in nums:
            if num in points: points[num] += num
            else: points[num] = num

        items = sorted(points.items())
        n = len(items)
        dp = [[0,0] for _ in range(n)]
        # [i][0] is skip, [i][1] is take
        dp[0][0] = 0
        dp[0][1] = items[0][1]
        prev = items[0][0]
        for i in range(1, n):
            num, amount = items[i]
            # overlap with previous element
            if prev == num - 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = dp[i-1][0] + amount
            # no overlap
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + amount

            prev = num

        return max(dp[~0])

    def deleteAndEarnBetter(self, nums: List[int]) -> int:
        points = dict()
        for num in nums:
            if num in points: points[num] += num
            else: points[num] = num

        keys = sorted(points.keys())
        n = len(keys)

        dp = [0 for _ in range(n)]
        dp[0] = points[keys[0]]
        skip = 0

        for i in range(1, n):
            num, amount = keys[i], points[keys[i]]

            if num-1 in points:
                dp[i] = max(dp[i-1], skip + amount)
            else:
                dp[i] = dp[i-1] + amount

            skip = dp[i-1]
            # print(f"num: {num:3}, amount: {amount:3}, skip: {skip:3}, take: {dp[i]:3}")

        return dp[~0]

    def deleteAndEarnBest(self, nums: List[int]) -> int:
        points = dict()
        for num in nums:
            if num in points: points[num] += num
            else: points[num] = num

        # print(sorted(points.items()))
        keys = sorted(points.keys())
        n = len(keys)

        take = points[keys[0]]
        skip = 0

        for i in range(1, n):
            num, amount = keys[i], points[keys[i]]

            if num-1 in points:
                temp = take
                take = skip + amount
                skip = max(skip, temp)
            else:
                skip = max(skip, take)
                take = skip + amount
            # print(f"num: {num:3}, amount: {amount:3}, skip: {skip:3}, take: {take:3}")

        return max(skip, take)


s = Solution()
cases = [([1], 1),
         ([1,3], 4),
         ([3,4,2], 6),
         ([2,2,2,2,3,3,4,4], 16),
         ([2,2,3,3,3,4], 9),
         ([8,7,3,8,1,4,10,10,10,2], 52),
         # ([10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5], 338)]
         ]

for case, expected in cases:
    assert s.deleteAndEarnFirstAttempt(case) == expected
    assert s.deleteAndEarnBetter(case) == expected
    assert s.deleteAndEarnBest(case) == expected
