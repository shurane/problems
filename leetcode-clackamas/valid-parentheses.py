# from colorama import init, Fore
# init()

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        for i, c in enumerate(s):
            # print(i, f"{s[:i]}{Fore.BLUE}{s[i]}{Fore.RESET}{s[i+1:]}", stack)

            if c in "([{":
                stack.append(c)
            else:
                peek = stack[-1] if stack else None
                if peek == "(" and c == ")" or peek == "[" and c == "]" or peek == "{" and c == "}" :
                    stack.pop()
                else:
                    # found unmatching parens
                    return False
        return len(stack) == 0

s = Solution()
assert s.isValid("") == True
assert s.isValid("()") == True
assert s.isValid("(()") == False
assert s.isValid("())") == False
assert s.isValid(")(") == False
assert s.isValid(")()") == False
assert s.isValid("()(") == False
assert s.isValid("[]") == True
assert s.isValid("{}") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(()[]{})") == True
assert s.isValid("(()[]{}") == False
assert s.isValid("()[]{})") == False