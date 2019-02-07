class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # grab bits in x, y
        # compare bits, left to right

        diff = 0
        # print "{:08b}".format(x), "{:08b}".format(y)
        while x > 0 or y > 0:
            # print x, y, "last bit", x & 0x1, y & 0x1
            diff += int((x & 0x1) != (y & 0x1))
            x = x >> 1
            y = y >> 1
        return diff
    
    def hammingDistance2(self, x: 'int', y: 'int') -> 'int':
        # print(format(x,'032b'), format(y,'032b'))

        count = 0
        for a, b in zip(format(x, '032b'), format(y, '032b')):
            if a != b:
                count += 1
        return count

    def hammingDistance3(self, x: 'int', y: 'int') -> 'int':
        # print(format(x,'032b'), format(y,'032b'))
        result = x ^ y
        count = 0
        while result > 0:
            count += result & 1
            result = result >> 1
        return count

s = Solution()

# print s.hammingDistance(1024, 1025)
# print s.hammingDistance(1024, 1026)
# print s.hammingDistance(1024, 1027)
# print s.hammingDistance(1024, 1028)
# print s.hammingDistance(1024, 1029)
# print s.hammingDistance(1024, 1030)
# print s.hammingDistance(1024, 1031)
# print s.hammingDistance(1024, 1032)
assert s.hammingDistance(1, 4) == 2
