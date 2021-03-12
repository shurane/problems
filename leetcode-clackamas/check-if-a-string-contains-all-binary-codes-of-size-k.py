class Solution3:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            b = format(i, 'b').zfill(k)
            if b not in s:
                return False
        return True

class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        i = 0
        total = 0
        seen = [False for i in range(2**k)]
        while i < len(s) - k + 1:
            window = s[i:i+k]
            number = int(window, 2)
            if not seen[number]:
                total += 1
                seen[number] = True
            i += 1
        return total == 2**k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        v = 0
        total = 0
        seen = [False for i in range(1 << k)]
        ones = (1 << k) - 1
        # print(s, k, ones, format(ones, 'b').zfill(k))
        for i, c in enumerate(s):
            v = v << 1 & ones | int(c)
            # print(i, c, v, format(v, 'b').zfill(k))
            if i >= k - 1 and not seen[v]:
                total += 1
                seen[v] = True
        # print(total)
        return total == 1 << k

s = Solution()

assert s.hasAllCodes("00110110", 2) == True
assert s.hasAllCodes("00110", 2) == True
assert s.hasAllCodes("0110", 1) == True
assert s.hasAllCodes("0000000001011100", 4) == False
assert s.hasAllCodes("0110", 2) == False
assert s.hasAllCodes("0000000100100011010001010110011110001001101010111100110111101111", 4) == True