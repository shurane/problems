class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # https://leetcode.com/problems/remove-k-digits/discuss/1779520/Python3-MONOTONIC-STACK-(oo)-Explained
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            if stack or digit is not "0":
                stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        return "".join(stack) or "0"

s = Solution()
assert s.removeKdigits("1432219", 3) == "1219"
assert s.removeKdigits("10200", 1) == "200"
assert s.removeKdigits("10", 2) == "0"
assert s.removeKdigits("112", 1) == "11"