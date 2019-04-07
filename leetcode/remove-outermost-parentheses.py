class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        primitives = []
        for i in range(len(S)):
            if S[i] == "(":
                stack.append(i)
            elif S[i] == ")":
                leftindex = stack.pop()
                if not stack:
                    primitives.append((leftindex, i))
        
        result = ""
        for left, right in primitives:
            result += S[left+1:right]
        return result

s = Solution()

assert s.removeOuterParentheses("") == ""
assert s.removeOuterParentheses("()") == ""
assert s.removeOuterParentheses("()()") == ""
assert s.removeOuterParentheses("(()())(())") == "()()()"
assert s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"

# 15 minutes