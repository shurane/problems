class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # what's the recurrence relation here?
        # it's very similar to best-time-to-buy-and-sell-stock

        # values[N] = max(values[N-1], values[N-2] + houses[N])
        # values[1] = houses[1]
        # values[0] = houses[0]

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        values = [ 0 for i in nums ]
        values[0] = nums[0]
        values[1] = max(nums[0], nums[1])

        i = 2
        while i < len(nums):
            values[i] = max(values[i-1], values[i-2] + nums[i])
            i += 1

        return values[-1]


s = Solution()

print s.rob([100,50,25])
print s.rob([])
print s.rob([100])
print s.rob([100,50])
