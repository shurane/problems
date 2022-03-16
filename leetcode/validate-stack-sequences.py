from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]
        i = 0
        j = 0
        while i < len(pushed) or j < len(popped):
            # print(f"pushed: {i}, popped: {j}, stack: {stack}")
            if stack[-1] != popped[j] and i != len(pushed):
                stack.append(pushed[i])
                i += 1
            elif stack[-1] == popped[j]:
                # print(f"matching, {stack[-1]} == {popped[j]}, popping")
                stack.pop()
                j += 1
            else:
                return False

        return stack == [-1]

    def validateStackSequencesLoop(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]
        j = 0
        for element in pushed:
            stack.append(element)
            while j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return stack == [-1]

    def validateStackSequencesConstantSpace(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        while i < len(pushed):
            # print("outer", pushed[i])
            ii = i
            while j < len(popped) and (pushed[ii] == popped[j] or pushed[ii] == -1):
                # print("inner", pushed[ii], popped[j])
                if pushed[ii] == popped[j]:
                    pushed[ii] = -1
                    j += 1
                ii -= 1
            i += 1
        # print("final", i, j, "expected:", len(pushed))
        return j == len(popped)

s = Solution()

testcases = [[[1,2,3], [3,2,1], True],
             [[1,2,3,4,5], [4,5,3,2,1], True],
             [[1,2,3,4,5], [4,3,5,1,2], False],
             [[2,1,0], [1,2,0], True],
             [[0], [0], True],
             [[0,1,2,3,4,5,6,7,8,9], [2,1,4,3,6,5,8,7,9,0], True],
             [[0,1,2,3,4,5,6,7,8,9], [3,6,9,8,7,5,4,2,1,0], True]]

for pushed, popped, expected in testcases:
    assert s.validateStackSequences(pushed, popped) == expected
    assert s.validateStackSequencesLoop(pushed, popped) == expected
    assert s.validateStackSequencesConstantSpace(pushed, popped) == expected
