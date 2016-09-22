MAXINT =  (2**31) - 1
MININT = -(2**31)
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """

        if not s:
            return 0

        s = s.strip()
        negative = 1
        result = 0
        nonDigitSeen = False

        # chop off the leading sign
        if s[0] == "-":
            negative = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        for c in s:
            if c in '0123456789' and not nonDigitSeen:
                result += ord(c) - ord('0')
                result *= 10
            elif c in '0123456789' and nonDigitSeen:
                # no more valid characters in string
                break
            else:
                # ignore non digit characters...
                nonDigitSeen = True

        result = result / 10
        result = negative * result

        if result > MAXINT:
            result = MAXINT
        if result < MININT:
            result = MININT

        return result
            
s = Solution()

assert s.myAtoi("") == 0

# tests for -i, i, +i as strings
for i in range(100):
    assert s.myAtoi(str(i)) == i
    assert s.myAtoi("+{}".format(i)) == i
    assert s.myAtoi("-{}".format(i)) == -i

# should strip whitespace off
for i in range(10):
    assert s.myAtoi(" " * i + "1") == 1

assert s.myAtoi("+-2") == 0
assert s.myAtoi("2garbage") == 2
assert s.myAtoi("-2garbage") == -2
assert s.myAtoi("  -0012a42") == -12

assert s.myAtoi(str(MAXINT + 1)) == MAXINT
assert s.myAtoi(str(MININT - 1)) == MININT
