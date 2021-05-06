from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) for i in nums]
        dp[-1] = 0

        # print("  nums", nums)
        # print("before", dp)
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            possibleJumps = range(i + 1, min(i + 1 + jump, len(nums)))
            # print(i, possibleJumps, [dp[j] for j in possibleJumps])
            if possibleJumps:
                dp[i] = min(dp[j] for j in possibleJumps) + 1
            else:
                dp[i] = len(nums)
        # print( " after", dp)

        return dp[0]

s = Solution()

assert s.jump([5,4,3,2,1,0]) == 1
assert s.jump([4,4,3,2,1,0]) == 2
assert s.jump([3,3,3,2,1,0]) == 2
assert s.jump([2,2,2,2,1,0]) == 3

assert s.jump([1,1,1,1,1,0]) == 5
assert s.jump([1,1,1,1,2,0]) == 5
assert s.jump([1,1,1,2,1,0]) == 4
assert s.jump([1,1,2,1,1,0]) == 4
assert s.jump([1,2,1,1,1,0]) == 4
assert s.jump([2,1,1,1,1,0]) == 4

assert s.jump([1,1,1,1,3,0]) == 5
assert s.jump([1,1,1,3,1,0]) == 4
assert s.jump([1,1,3,1,1,0]) == 3
assert s.jump([1,3,1,1,1,0]) == 3
assert s.jump([3,1,1,1,1,0]) == 3

assert s.jump([2,0,2,0,2,0]) == 3

assert s.jump([2,3,1,1,4]) == 2
assert s.jump([2,3,0,1,4]) == 2
assert s.jump([1,3,2,3,1,0]) == 3