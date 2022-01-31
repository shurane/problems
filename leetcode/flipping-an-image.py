from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i = 0
            N = len(row)
            while i * 2 < N:
                # swap
                # row[i], row[N - i - 1] = row[N - i - 1], row[i]

                # # invert 0s to 1s and vice versa
                # row[i] = 1 - row[i]
                # row[N - i - 1] = 1 - row[N - i - 1]

                i += 1

            # if N % 2 == 1:
            #     row[N // 2] = 1 - row[N // 2]

        return A

    def flipAndInvertImage2(self, A: List[List[int]]) -> List[List[int]]:

        # drew inspiration from https://leetcode.com/problems/flipping-an-image/discuss/130590/C++JavaPython-Reverse-and-Toggle
        for row in A:
            i = 0
            N = len(row)
            while i * 2 < N:
                if row[i] == row[N - i - 1]:
                    row[i] = row[N - i - 1] = 1 - row[i]

                i += 1
        return A


s = Solution()

assert s.flipAndInvertImage([[0],[0],[0]]) == [[1],[1],[1]]
assert s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]

# 10 minutes