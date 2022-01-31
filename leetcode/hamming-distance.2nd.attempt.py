class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # print(format(x,'032b'), format(y,'032b'))

        count = 0
        for a, b in zip(format(x, '032b'), format(y, '032b')):
            if a != b:
                count += 1
        return count

    def hammingDistance2(self, x: int, y: int) -> int:
        # print(format(x,'032b'), format(y,'032b'))
        result = x ^ y
        count = 0
        while result > 0:
            count += result & 1
            result = result >> 1
        return count

s = Solution()
assert s.hammingDistance2(1, 4) == 2
assert s.hammingDistance2(1, 2**31-1) == 30

# 14 minutes