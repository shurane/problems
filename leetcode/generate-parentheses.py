from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        stack = [("", n, n)]

        while stack:
            s, open_, close = stack.pop()

            if open_ == 0 and close == 0:
                results.append(s)

            if open_ < close:
                stack.append((s + ")", open_, close - 1))

            if open_ > 0:
                stack.append((s + "(", open_ - 1, close))

        return results

s = Solution()
assert s.generateParenthesis(1) == ["()"]
assert s.generateParenthesis(2) == ["(())","()()"]
assert s.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]