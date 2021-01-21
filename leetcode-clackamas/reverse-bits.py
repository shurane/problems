class Solution:
    def reverseBits(self, n: int) -> int:
        m = n
        result = 0
        # get bits out one at a time and then bitshift right
        # add to end of another number and then bitshift left
        for i in range(32):
            last = m & 1
            result = result << 1
            result += last
            m = m >> 1

        # print(n, m, result)
        # https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros-in-python
        # print("n", format(n, "032b"))
        # print("m", format(m, "032b"))
        # print("r", format(result, "032b"))
        return result


s = Solution()

assert s.reverseBits(2**32 - 1) == 2**32 - 1
assert s.reverseBits(0) == 0
assert s.reverseBits(43261596) == 964176192
assert s.reverseBits(4294967293) == 3221225471

