class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 or x > 2**31:
            return False

        # digits = []
        copy = x
        y = 0
        while x > y:
            # digits.append(x % 10)
            y = y * 10 + (x % 10)
            x = int(x / 10)

        # print(digits)
        # return digits == list(reversed(digits))
        # print(y)
        return y == copy

s = Solution()
assert s.isPalindrome(-1) == False
assert s.isPalindrome(0) == True
assert s.isPalindrome(1) == True
assert s.isPalindrome(50) == False
assert s.isPalindrome(55) == True
assert s.isPalindrome(737) == True
assert s.isPalindrome(773) == False
assert s.isPalindrome(-2147447412) == False