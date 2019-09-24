class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # print(c, stack)
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

s = Solution()

assert s.isValid("") == True
assert s.isValid("(") == False
assert s.isValid("[") == False
assert s.isValid("{") == False
assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("([{}])") == True
assert s.isValid("([)]") == False
assert s.isValid("([)") == False
assert s.isValid("(][)") == False
assert s.isValid("][") == False
assert s.isValid("}{") == False
assert s.isValid(")(") == False