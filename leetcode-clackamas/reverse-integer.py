class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        y = abs(x)
        result = 0
        while y > 0:
            digit = y % 10
            y = y // 10

            result *= 10
            result += digit

            if result > 2**31 -1 or result < -2**31:
                return 0
        return sign * result

# test cases: 123, -123, 1, 0, -1, 2147483647, -2147483648
