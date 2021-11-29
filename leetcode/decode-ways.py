values = [str(i) for i in range(1, 27)]

def decode(digits):
    return digits in values

class Solution:
    def numDecodings(self, s: str) -> int:
        # A[n] = A[n-1] + A[n-2:n]
        # A[i] = A[i-1] if decode(S[i])
        #      + A[i-2] if decode(S[i-2:i])
        # A[1] = 0 or 1 or 2
        # A[0] = 0 or 1
        # It's a lot like fibonacci...
        # the recursive solution is way easier to write than the iterative solution

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return int(decode(s))
        elif len(s) == 2:
            return int(decode(s)) + int(decode(s[0]) and decode(s[1]))

        A = [0 for c in s]
        A[0] = int(decode(s[0]))
        A[1] = int(decode(s[0:2])) + int(decode(s[0]) and decode(s[1]))

        for i in range(2, len(s)):
            total = 0

            # print(f"checking {s[i]}")
            if decode(s[i]):
                total += A[i-1]

            # print(f"checking {s[i-1:i+1]}")
            if decode(s[i-1:i+1]):
                total += A[i-2]

            A[i] = total

        return A[-1]

    def numDecodingsRedux(self, s: str) -> int:
        s = [int(i) for i in s]
        # no ways to decode '0', 1 way to decode other digits
        last = int(s[~0] != 0)
        if len(s) == 1:
            return last

        # separate returns either 1 or 0 depending on the current and the character ahead of it
        separate = int(s[~1] != 0) * last
        # first digit is not '0' and value is within the range of a-z
        tens = s[~1] * 10
        ones = s[~0]
        value = tens + ones
        together = int(tens != 0 and 0 < value < 27)
        # penultimate
        pen = separate + together

        # TODO there should be a way to simplify this for loop
        for i in range(2, len(s)):
            separate = int(s[~i] != 0) * pen
            tens = s[~i] * 10
            ones = s[~(i-1)]
            value = tens + ones
            together = int(tens != 0 and 0 < value < 27) * last

            # print(s, f"i: {i}, separate:{separate}, value: {value:2}, together: {together}, pen: {pen}, last:{last}")
            last = pen
            pen = separate + together

        return pen

s = Solution()
assert s.numDecodings("") == 0
assert s.numDecodings("0") == 0
assert s.numDecodings("1") == 1
assert s.numDecodings("2") == 1
assert s.numDecodings("3") == 1
assert s.numDecodings("4") == 1
assert s.numDecodings("5") == 1
assert s.numDecodings("6") == 1
assert s.numDecodings("7") == 1
assert s.numDecodings("8") == 1
assert s.numDecodings("9") == 1
assert s.numDecodings("10") == 1 # (10)
assert s.numDecodings("11") == 2 # (11), (1, 1)
assert s.numDecodings("12") == 2 # (12), (1, 2)
assert s.numDecodings("20") == 1 # (20)
assert s.numDecodings("26") == 2 # (26), (2, 6)
assert s.numDecodings("27") == 1 # (2, 7)
assert s.numDecodings("30") == 0
assert s.numDecodings("63") == 1 # (6,3)
assert s.numDecodings("77") == 1 # (7,7)
assert s.numDecodings("00") == 0
assert s.numDecodings("100") == 0
assert s.numDecodings("111") == 3 # (11, 1), (1, 11), (1, 1, 1)
assert s.numDecodings("666") == 1 # (6, 6, 6)
assert s.numDecodings("777") == 1 # (7, 7, 7)
assert s.numDecodings("007") == 0
assert s.numDecodings("1001") == 0
assert s.numDecodings("1010") == 1 # (10, 10)
assert s.numDecodings("10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
assert s.numDecodings("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 16374361185569570355515148989381228747223756609038926650176124155306760699

assert s.numDecodingsRedux("0") == 0
assert s.numDecodingsRedux("1") == 1
assert s.numDecodingsRedux("2") == 1
assert s.numDecodingsRedux("3") == 1
assert s.numDecodingsRedux("4") == 1
assert s.numDecodingsRedux("5") == 1
assert s.numDecodingsRedux("6") == 1
assert s.numDecodingsRedux("7") == 1
assert s.numDecodingsRedux("8") == 1
assert s.numDecodingsRedux("9") == 1
assert s.numDecodingsRedux("06") == 0
assert s.numDecodingsRedux("10") == 1
assert s.numDecodingsRedux("11") == 2
assert s.numDecodingsRedux("20") == 1
assert s.numDecodingsRedux("21") == 2
assert s.numDecodingsRedux("22") == 2
assert s.numDecodingsRedux("27") == 1
assert s.numDecodingsRedux("30") == 0
assert s.numDecodingsRedux("31") == 1
assert s.numDecodingsRedux("32") == 1
assert s.numDecodingsRedux("33") == 1
assert s.numDecodingsRedux("40") == 0
assert s.numDecodingsRedux("90") == 0
assert s.numDecodingsRedux("99") == 1
assert s.numDecodingsRedux("111") == 3
assert s.numDecodingsRedux("106") == 1
assert s.numDecodingsRedux("666") == 1
assert s.numDecodingsRedux("777") == 1
assert s.numDecodingsRedux("1001") == 0
assert s.numDecodingsRedux("1106") == 1
assert s.numDecodingsRedux("11106") == 2
assert s.numDecodingsRedux("226") == 3
assert s.numDecodingsRedux("10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010") == 1
assert s.numDecodingsRedux("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 16374361185569570355515148989381228747223756609038926650176124155306760699
