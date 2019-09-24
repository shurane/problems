from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alex never loses...
        return True

    def stoneGameScoreDiff(self, piles: List[int]) -> int:
        # https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
        # more interesting if:
        #   - we return the difference in score
        #   - we don't know if len(piles) is even
        if len(piles) == 1:
            return piles[0]
        elif len(piles) == 2:
            return abs(piles[0] - piles[1])
        else:
            # TODO this is only optimal for Alex and not for Lee
            # lee215 mentions this as a 2D DP problem
            return max(piles[ 0] - piles[ 1]      + self.stoneGameScoreDiff(piles[2: ]),
                       piles[-1] - piles[-2]      + self.stoneGameScoreDiff(piles[:-2]),
                       abs(piles[ 0] - piles[-1]) + self.stoneGameScoreDiff(piles[1:-1]))

s = Solution()
assert s.stoneGame([5,2]) == True
assert s.stoneGame([1,10,9,1]) == True
assert s.stoneGame([5,3,4,5]) == True
assert s.stoneGame([3,3,4,5]) == True
assert s.stoneGame([1,2,3,8,10,5]) == True
assert s.stoneGame([1,10,1,1,1,1,2,1,10,1]) == True

assert s.stoneGameScoreDiff([5,2]) == 3
assert s.stoneGameScoreDiff([1,10,9,1]) == 1
assert s.stoneGameScoreDiff([5,3,4,5]) == 1
assert s.stoneGameScoreDiff([3,3,4,5]) == 1
assert s.stoneGameScoreDiff([1,2,3,8,10,5]) == 1
assert s.stoneGameScoreDiff([1,10,1,1,1,1,2,1,10,1]) == 1