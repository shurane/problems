from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return self.sortedSquaresInsideOut2(A)

    def sortedSquaresOutsideIn(self, A):
        ## outside in, O(n)
        B = [0] * len(A)

        l, r = 0, len(A) - 1

        while l <= r:
            l2, r2 = A[l] ** 2, A[r] ** 2
            if l2 > r2:
                B[r - l] = l2
                l += 1
            else:
                B[r - l] = r2
                r -= 1
        return B

    def sortedSquaresBisect(self, A: List[int]) -> List[int]:
        ## first solution, O(nlogn)
        import bisect
        B = []
        for num in A:
            bisect.insort(B, num**2) # O(nlogn)
        return B

    def sortedSquaresSquareThenSort(self, A: List[int]) -> List[int]:
        ## second solution, O(nlogn)
        for i in range(len(A)):
            A[i] = A[i]**2
        return sorted(A) # O(nlogn)

    def sortedSquaresInsideOut(self, A: List[int]) -> List[int]:
        import sys
        ## O(n), makes 2 passes, but slower runtime than the O(nlogn) solutions
        ## I guess this is inside out?
        B = [0] * len(A)
        index = len(A) - 1

        ## search for the first non negative value
        for i in range(len(A)):
            if A[i] >= 0:
                index = i
                break


        l, r = index - 1, index
        l2, r2 = A[l] ** 2, A[r] ** 2
        while r - l < len(A) + 1:

            if r >= len(A):
                r2 = sys.maxsize
            else:
                r2 = A[r] ** 2
            if l < 0:
                l2 = sys.maxsize
            else:
                l2 = A[l] ** 2

            if l2 < r2:
                B[r - l - 1] = l2
                l -= 1
            else:
                B[r - l - 1] = r2
                r += 1
        return B

    def sortedSquaresInsideOut2(self, A: List[int]) -> List[int]:
        ## One more attempt, inspired by https://leetcode.com/problems/squares-of-a-sorted-array/discuss/224318/Python-O(N)-beats-100
        B = [0] * len(A)
        index = len(A) - 1

        ## search for the first non negative value
        for i in range(len(A)):
            if A[i] >= 0:
                index = i
                break

        l, r = index - 1, index
        while r - l < len(A) + 1:

            ## move l,r pointers to other end if they exceed the bounds
            li = len(A) - 1 if l < 0 else l
            ri = 0 if r >= len(A) else r
            l2, r2 = A[li] ** 2, A[ri] ** 2
            # print(l, r, l2, r2)

            if l2 < r2:
                B[r - l - 1] = l2
                l -= 1
            else:
                B[r - l - 1] = r2
                r += 1
        return B


input1 = [-4,-1,0,3,10]
input2 = [-9,-8,-7,-6,-5]
input3 = [5,6,7,8,9]
input4 = [1,1,1,1,1]
input5 = [-1,-1,-1,-1,-1]

s = Solution()
assert s.sortedSquares(input1) == [0,1,9,16,100]
assert s.sortedSquares(input2) == [25,36,49,64,81]
assert s.sortedSquares(input3) == [25,36,49,64,81]
assert s.sortedSquares(input4) == [1,1,1,1,1]
assert s.sortedSquares(input5) == [1,1,1,1,1]

# 45min+