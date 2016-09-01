letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [str(ord(c) - 64) for c in letters]

def decode(digits):
    return digits in values

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A[n] = A[n-1] + A[n-2:n]
        # A[i] = A[i-1] if decode(S[i]) 
        #      + A[i-2] if decode(S[i-2:i])
        # A[1] = 1 or 2
        # A[0] = 1
        # It's a lot like fibonacci...
        # the recursive solution is way easier to write than the iterate solution

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return int(decode(s))
        elif len(s) == 2:
            return int(decode(s)) + int(decode(s[0]) and decode(s[1]))

        A = [0 for c in s]
        A[0] = int(decode(s[0]))
        A[1] = int(decode(s[0:2])) + int(decode(s[0]) and decode(s[1]))

        for i in xrange(2, len(s)):
            total = 0
            
            # print "checking {}".format(s[i])
            if decode(s[i]):
                total += A[i-1]
            
            # print "checking {}".format(s[i-1:i+1])
            if decode(s[i-1:i+1]):
                total += A[i-2]

            A[i] = total

        return A[-1]

s = Solution()
assert s.numDecodings("") == 0
assert s.numDecodings("1") == 1
assert s.numDecodings("9") == 1
assert s.numDecodings("10") == 1 # (10)
assert s.numDecodings("11") == 2 # (11), (1, 1)
assert s.numDecodings("12") == 2 # (12), (1, 2)
assert s.numDecodings("26") == 2 # (26), (2, 6)
assert s.numDecodings("27") == 1 # (27)
assert s.numDecodings("63") == 1 # (6,3)
assert s.numDecodings("77") == 1 # (7,7)
assert s.numDecodings("100") == 0 
assert s.numDecodings("111") == 3 # (11, 1), (1, 11), (1, 1, 1)
assert s.numDecodings("666") == 1 # (6, 6, 6)
assert s.numDecodings("777") == 1 # (7, 7, 7)
assert s.numDecodings("007") == 0
assert s.numDecodings("1010") == 1
assert s.numDecodings("10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
print s.numDecodings("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
