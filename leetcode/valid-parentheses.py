class Solution:
    def isValidFirst(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter in "({[":
                stack.append(letter)
            else:
                if not stack:
                    return False

                left = stack.pop()

                if left == "(" and letter == ")":
                    pass
                elif left == "{" and letter == "}":
                    pass
                elif left == "[" and letter == "]":
                    pass
                else:
                    return False
        return not stack

    def isValid(self, s: str) -> bool:
        # inspired from https://leetcode.com/problems/valid-parentheses/discuss/9178/Short-java-solution
        stack = []
        for letter in s:
            if   letter == "(": stack.append(")")
            elif letter == "{": stack.append("}")
            elif letter == "[": stack.append("]")
            else:
                if not stack or letter != stack.pop():
                    return False
        return not stack

