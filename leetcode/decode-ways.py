letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [str(ord(c) - 64) for c in letters]
map = dict(zip(values, letters))

def decode(digits):
    return digits in map

class Solution(object):

    def numDecodings2(self, s):
        # print "numDecodings2({})".format(s)
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return int(decode(s))
        elif len(s) == 2:
            return int(decode(s)) + int(decode(s[0]) and int(decode(s[1])))
        else:
            total = 0
            if decode(s[-1:]):
                # print "recurring on... {}".format(s[:-1])
                total += self.numDecodings2(s[:-1])
            if decode(s[-2:]):
                # print "recurring on... {}".format(s[:-2])
                total += self.numDecodings2(s[:-2])

            return total

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

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return int(decode(s))
        elif len(s) == 2:
            return int(decode(s)) + int(decode(s[0]) and int(decode(s[1])))

        A = [0 for c in s]
        A[0] = int(decode(s[0]))

        if A[0] == 0:
            A[1] = 0
        else:
            total = 0
            if decode(s[0]) and decode(s[1]):
                total += 1
            if decode(s[0:2]):
                total += 1
            A[1] = total

        for i in xrange(2, len(s)):
            total = 0
            
            if decode(s[i]):
                total += A[i-1]
            
            if decode(s[i-2:i]):
                total += A[i-2]


            if A[i-1] == 0 or not (decode(s[i]) and decode(s[i-2:i])):
                A[i] = 0
            else:
                A[i] = total

            print A

        return A[-1]
        

s = Solution()
assert s.numDecodings2("") == 0
assert s.numDecodings2("1") == 1
assert s.numDecodings2("9") == 1
assert s.numDecodings2("10") == 1 # (10)
assert s.numDecodings2("11") == 2 # (11), (1, 1)
assert s.numDecodings2("12") == 2 # (12), (1, 2)
assert s.numDecodings2("26") == 2 # (26), (2, 6)
assert s.numDecodings2("27") == 1 # (27)
assert s.numDecodings2("100") == 0 
assert s.numDecodings2("111") == 3 # (11, 1), (1, 11), (1, 1, 1)
assert s.numDecodings2("666") == 1 # (6, 6, 6)
assert s.numDecodings2("777") == 1 # (7, 7, 7)
assert s.numDecodings2("007") == 0
assert s.numDecodings2("1010") == 1
assert s.numDecodings2("10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
