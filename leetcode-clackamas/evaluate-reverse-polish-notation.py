from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {
            "-": lambda x,y: x-y,
            "+": lambda x,y: x+y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: int(x/y)
        }
        for token in tokens:
            if token in "-+*/":
                right = s.pop()
                left = s.pop()
                op = ops[token]
                result = op(left, right)
                # print(f"{left} {token} {right} = {result}")
                s.append(result)
            else:
                s.append(int(token))

        # print(s)
        return s[-1]

s = Solution()
assert s.evalRPN(["2","1","+","3","*"]) == 9
assert s.evalRPN(["4","13","5","/","+"]) == 6
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert s.evalRPN(["-30","7","/"]) == -4
assert s.evalRPN(["-7","30","/"]) == 0
assert s.evalRPN([" 7","30","/"]) == 0