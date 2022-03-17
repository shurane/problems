class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper():
            nonlocal i
            score = 0
            while i < len(s):
                if s[i] == "(" and s[i+1] == ")":
                    i += 2
                    score += 1
                elif s[i] == "(":
                    i += 1
                    score += helper() * 2
                else: # s[i] == ")"
                    i += 1
                    return score
            return score

        i = 0
        return helper()

    def scoreOfParenthesesStack(self, s: str) -> int:
        stack = [0]

        i = 0
        while i < len(s):
            if s[i] == "(" and s[i+1] == ")":
                i += 2
                stack[-1] += 1
            elif s[i] == "(":
                i += 1
                stack.append(0)
            else: # s[i] == ")"
                i += 1
                value = stack.pop() * 2
                stack[-1] += value

        return stack[-1]

    def scoreOfParenthesesStackSimpler(self, s: str) -> int:
        stack = []
        value = 0

        for letter in s:
            if letter == "(":
                stack.append(value)
                value = 0
            else:
                # when value == 0, return 1 because "()" is 1
                # otherwise value += value, which doubles it.
                # Neat. Tricky, though
                value += stack.pop() + max(value, 1)

        return value

s = Solution()

testcases = [["()", 1],
             ["()()", 2],
             ["()()()", 3],
             ["(())", 2],
             ["((()))", 4],
             ["((()))((()))((()))", 12],
             ["(((()))((()))((())))", 24],
             ["(())()", 3],
            ]

for case, expected in testcases:
    assert s.scoreOfParentheses(case) == expected
    assert s.scoreOfParenthesesStack(case) == expected
    assert s.scoreOfParenthesesStackSimpler(case) == expected
