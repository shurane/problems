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

    # lot of ideas... but still somewhat hard for me to follow
    # if I understand right, at each step of multiplying between X and Y, it needs to figure out if it should subtract by 1 (aka set a bit)
    # still doesn't make complete sense to me, though
    # https://leetcode.com/problems/broken-calculator/discuss/308539/Thinking-Forward
    # https://leetcode.com/problems/broken-calculator/discuss/1878207/Fast-Python-forward-solution
    # https://leetcode.com/problems/broken-calculator/discuss/1877249/Forward-solution-oror-Python
    def brokenCalcForwards(self, X: int, Y: int) -> int:
        count = 0
        while X < Y:
            X *= 2
            count += 1

        left = X - Y
        power = count

        while left > 0:
            count += left // 2**power
            left %= 2 ** power
            power -= 1

        return count

s = Solution()

assert s.brokenCalc(2, 3) == 2
assert s.brokenCalc(5, 8) == 2
assert s.brokenCalc(7, 21) == 5

assert s.brokenCalcForwards(2, 3) == 2
assert s.brokenCalcForwards(5, 8) == 2
assert s.brokenCalcForwards(7, 21) == 5

