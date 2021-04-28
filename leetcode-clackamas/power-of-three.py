from itertools import takewhile, count

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-three/discuss/751445/Python3-a-few-approaches
        # I kind of follow this but don't follow the conditions for True vs False
        # basically you're dividing n by 3 and checking the remainder, repeatedly.
        if n == 0: return False
        while n > 1:
            n, r = divmod(n, 3)
            if r > 0: return False
        return True

    def isPowerOfThree2(self, n: int) -> bool:
        i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 3
        return False

s = Solution()
powers = list(takewhile(lambda x: x < 2**31 - 1, (3 ** i for i in count())))

for p in powers:
    assert s.isPowerOfThree(p) == True
    assert s.isPowerOfThree(p - 1) == False
    assert s.isPowerOfThree(p + 1) == False