from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            # print(f"i:{i:2}, A[i]:{A[i]:2}, {abs(A[i] - i)}")
            if abs(A[i] - i) > 1:
                return False

        return True

s = Solution()

assert s.isIdealPermutation([1,0,2]) == True
assert s.isIdealPermutation([1,2,0]) == False
assert s.isIdealPermutation(list(range(50))) == True
assert s.isIdealPermutation(list(reversed(range(50)))) == False

assert s.isIdealPermutation([0,1,2,3,4,5,6,7,8,9]) == True
assert s.isIdealPermutation([1,0,3,2,5,4,7,6,9,8]) == True
assert s.isIdealPermutation([1,2,3,4,5,6,7,8,9,0]) == False