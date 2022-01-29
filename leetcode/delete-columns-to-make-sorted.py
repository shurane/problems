from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        length = len(A)
        width = len(A[0])

        indexes = []
        for i in range(width):
            # check two words at a time
            for j in range(length - 1):
                if A[j][i] <= A[j+1][i]:
                    pass
                else:
                    indexes.append(i)
                    break
        # print(indexes)
        return len(indexes)

s = Solution()

assert s.minDeletionSize(["b","a"]) == 1 # is this valid? then it just becomes ["", ""]
assert s.minDeletionSize(["a","b"]) == 0
assert s.minDeletionSize(["cba","daf","ghi"]) == 1
assert s.minDeletionSize(["zyx","wvu","tsr"]) == 3

# 6 minutes