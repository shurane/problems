class Solution:
    def selfDividingNumbers(self, left: 'int', right: 'int') -> 'List[int]':
        matches = []
        for i in range(left, right + 1):
            j = i
            div = True
            while j > 0:
                digit = j % 10
                if digit == 0:
                    div = False
                    break
                elif i % digit != 0:
                    div = False
                    break
                j = j // 10
            if div:
                matches.append(i)
        return matches
        

s = Solution()

assert s.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert s.selfDividingNumbers(128, 128) == [128]

# 2 minutes