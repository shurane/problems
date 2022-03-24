class Solution:
    # https://leetcode.com/problems/broken-calculator/discuss/1076061/Broken-Calculator-or-JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Detailed-Explanation
    # going backwards, so using `div 2` and `plus 1` operations
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while Y > X:
            # print(Y, X, count)
            if Y % 2 == 0:
                Y = Y // 2
            else:
                Y += 1
            count += 1
        return X - Y + count

s = Solution()

assert s.brokenCalc(2, 3) == 2
assert s.brokenCalc(5, 8) == 2
assert s.brokenCalc(7, 21) == 5

