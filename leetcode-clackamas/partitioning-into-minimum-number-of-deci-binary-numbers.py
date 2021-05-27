class Solution:
    def minPartitions(self, n: str) -> int:
        l = 0
        for d in n:
            i = int(d)
            if i > l:
                l = i
        return l

s = Solution()
assert s.minPartitions("32") == 3
assert s.minPartitions("82734") == 8
assert s.minPartitions("27346209830709182346") == 9