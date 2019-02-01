class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # clever, because of the constraints of the problem, you can scan a window through the list for the repeated element
        for i in range(0, len(A)-2):
            if A[i] == A[i+1] or A[i] == A[i+2] or A[i] == A[i+3]:
                return A[i]
            elif A[i+1] == A[i+2] or A[i+1] == A[i+3]:
                return A[i+1]
            elif A[i+2] == A[i+3]:
                return A[i+2]
        
        return None
    
s = Solution()
assert s.repeatedNTimes([1,2,3,3]) == 3
assert s.repeatedNTimes([9,5,6,9]) == 9
assert s.repeatedNTimes([2,1,2,5,3,2]) == 2
assert s.repeatedNTimes([2,2,2,5,3,1]) == 2
assert s.repeatedNTimes([3,1,5,2,2,2]) == 2

# 10 minutes 0 seconds