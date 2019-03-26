class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = dict()
        i = 0
        while i < len(nums):
            left = target - nums[i]
            if left in visited:
                return [visited[left], i]
            
            visited[nums[i]] = i
            i += 1
        
        return [-1, -1]

s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))