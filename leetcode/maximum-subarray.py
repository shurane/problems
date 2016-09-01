class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # this solution doesn't work because M[n-1] isn't an intermediate step
        # M[n] = max(M[n-1] + A[n], M[n-1], A[n])
        # M[0] = A[0]


        # I see... so it resets if the A[n] is way higher than any of the
        # previous sums. It's sort of like range-sum-query with the partial
        # sums, but resets if the current value is greater

        # M[n] = max(M[n-1] + A[n], A[n])
        # M[0] = A[0]
        
        # TODO There's a divide and conquer way, how does that work?

        # maxes = [nums[0] for i in nums]
        # highest = nums[0]
        # for i in xrange(1, len(nums)):
            # maxes[i] = max(maxes[i-1] + nums[i],
                           # # maxes[i-1],
                                        # nums[i])
            # if maxes[i] > highest:
                # highest = maxes[i]

        highest = nums[0]
        prev = nums[0]

        for i in xrange(1, len(nums)):
            temp = max(prev + nums[i], nums[i])

            if temp > highest:
                highest = temp

            prev = temp

        return highest
        
        
s = Solution()
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert s.maxSubArray([100,-1,-1,-1,-1,-1,-1,100]) == 194
assert s.maxSubArray([-1,-1,-1,-1,100,-1,-1,100]) == 198
assert s.maxSubArray([1]) == 1
