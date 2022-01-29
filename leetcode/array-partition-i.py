class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        total = 0
        while i < len(nums) // 2:
            # total += min(nums[i*2], nums[i*2 + 1])
            total += nums[i*2]
            i += 1
        return total

s = Solution()

assert s.arrayPairSum([1,4,3,2]) == 4
assert s.arrayPairSum([1,1]) == 0