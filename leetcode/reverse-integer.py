class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = []
        negative = 1
        if x < 0:
            negative = -1
            x = abs(x)

        while x > 0:
            digits.append(x % 10)
            x /= 10

        result = 0

        for i, digit in enumerate(reversed(digits)):
            result += digit * 10**i

        # for numbers that overflow a regular int32
        if result > 2**31-1:
            result = 0

        return result * negative

s = Solution()

assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(1534236469) == 0
assert s.reverse(1563847412) == 0
