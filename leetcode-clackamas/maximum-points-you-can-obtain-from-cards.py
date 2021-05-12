from typing import List

class Solution:
    def maxScoreRecursive(self, cardPoints: List[int], k: int) -> int:
        cache = dict()
        score = self.helper(cardPoints, k, 0, len(cardPoints) - 1, cache)
        # print(score)
        return score

    def helper(self, cardPoints, k, l, r, cache):
        if k == 1:
            return max(cardPoints[l], cardPoints[r])
        elif (l,r) in cache:
            return cache[(l,r)]
        else:
            score = max(self.helper(cardPoints, k - 1, l + 1, r    , cache) + cardPoints[l],
                        self.helper(cardPoints, k - 1, l    , r - 1, cache) + cardPoints[r])
            cache[(l,r)] = score
            return score

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        left = 0
        right = sum(cardPoints[r:])
        score = left + right
        # print(f"beginning {left:3}, {right:3}, {score:4}, {l:3}, {r:3}, {cardPoints[r:]}")
        for i in range(0, k):
            left += cardPoints[l + i]
            right -= cardPoints[r + i]
            score = max(score, left + right)
            # print(f"     loop {left:3}, {right:3}, {left + right:4}, {l+i:3}, {r+i:3}")

        # print("final score", score)
        return score

s = Solution()

assert s.maxScore([1,2,3,4,5,6], 3) == 15
assert s.maxScore([6,5,4,3,2,1], 3) == 15

assert s.maxScore([1,2,3,4,5,6,1], 3) == 12
assert s.maxScore([2,2,2], 2) == 4
assert s.maxScore([9,7,7,9,7,7,9], 7) == 55
assert s.maxScore([1,1000,1], 1) == 1
assert s.maxScore([1,79,80,1,1,1,200,1], 3) == 202
assert s.maxScore([50,40,17,25,100,75], 3) == 225
assert s.maxScore([100,40,17,9,73,75], 3) == 248

import random
random.seed(0)
lst = [random.randint(1, 1000) for i in range(10000)]
k = len(lst) // 2
# print(k, lst[:100])
assert s.maxScore(lst, k) == 2528779