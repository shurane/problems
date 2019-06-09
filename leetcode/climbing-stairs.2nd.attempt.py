class Solution:
    def climbStairs(self, n: int) -> int:
        # O(n) time, O(1) space
        if n == 1:
            return 1

        prev2 = 1
        prev1 = 1

        for _ in range(2, n + 1):
            succ = prev2 + prev1
            prev2 = prev1
            prev1 = succ
        return succ

    def climbStairs2nd(self, n: int) -> int:
        # O(n) time, O(n) space
        if n == 1:
            return 1

        waysToClimb = [None] * (n + 1)
        waysToClimb[0] = 1
        waysToClimb[1] = 1

        for i in range(2, n + 1):
            waysToClimb[i] = waysToClimb[i-1] + waysToClimb[i-2]
        return waysToClimb[n]

# from discussion, "basically it's a fibonacci" https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
# didn't realize that. Makes sense. I guess I can start with (0, 1), (1, 1), or even (1, 2) for this.

s = Solution()

assert s.climbStairs(1) == 1
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5