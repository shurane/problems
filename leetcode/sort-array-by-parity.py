from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 == 1 and A[j] %2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[i] % 2 == 0:
                i += 1
            else:
                j -= 1

        return A

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))
print(s.sortArrayByParity(list(range(10))))
print(s.sortArrayByParity([2,2,2,2,2,2]))
print(s.sortArrayByParity([1,1,1,1,1,1]))

print(s.sortArrayByParity([2,1,1,1,1,1]))
print(s.sortArrayByParity([1,2,2,2,2,2]))

# 8 minutes