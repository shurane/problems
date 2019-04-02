class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        y = 0

        while x != 0:
            y = y * 10 + (x % 10)
            x = x / 10 # python 2

        y *= sign

        if y > 2**31 - 1 or y < -2**31:
            y = 0

        return y

s = Solution()
print(s.reverse(500))
print(s.reverse(-500))
print(s.reverse(-123))
print(s.reverse(123))
print(s.reverse(-321))
print(s.reverse(321))
print(s.reverse(2147483648))
print(s.reverse(1111111111))
print(s.reverse(1111111112))
print(s.reverse(1111111113))