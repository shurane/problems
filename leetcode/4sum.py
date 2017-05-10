

class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pass

    def fourSumSlow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        #brute force approach would be n**4, 4 for loops

        n = len(nums)
        quadruplets = []
        for i in range(n):
            for j in range (i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quadruplets.append([nums[i],nums[j],nums[k],nums[l]])
        return quadruplets
        

s = Solution()

print s.fourSumSlow([1, 0, -1, 0, -2, 2], 0)
