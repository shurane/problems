class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        negative = 1

        if x < 0:
            negative = -1
            x = abs(x)

        while x > 0:
            result *= 10
            result += (x % 10)
            x /= 10

        if result > 2147483647:
            result = 0

        return result * negative

    def reverseStr(self, x):
        negative = 1
        if x < 0:
            negative = -1
        result = int(str(abs(x))[::-1])
        if result > 2**31-1:
            result = 0
        return result * negative

s = Solution()

assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(1534236469) == 0
assert s.reverse(1563847412) == 0
assert s.reverse(0) == 0
