from typing import List
from helpers2 import compareListOfLists

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        results = []

        for i in range(0, len(nums) - 2):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                # print("duplicate found:", nums[i], "skipping")
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                # print(f"i: {i}, l: {l}, r: {r}")
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    # print("success", [nums[i], nums[l], nums[r]])
                    triplet = [nums[i], nums[l], nums[r]]
                    results.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        # print("duplicate found with l:", nums[l], "skipping")
                        l += 1
                    while r > l and nums[r] == triplet[2]:
                        # print("duplicate found with r:", nums[r], "skipping")
                        r -= 1
        # print(results)
        return results

    def threeSumSlow(self, nums):
        results = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums) - 1):
                if j > i+1 and nums[j] == nums[j-1]: continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]: continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        # print(results)
        return results

s = Solution()

assert compareListOfLists(s.threeSum([0, 0]), [])
assert compareListOfLists(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
assert compareListOfLists(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
assert compareListOfLists(s.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
assert compareListOfLists(s.threeSumSlow([-1,-1,0,0,0,0,0,1,1]), [[-1,0,1], [0,0,0]])
assert compareListOfLists(s.threeSum([-1,-1,0,0,0,0,0,1,1]), [[-1,0,1], [0,0,0]])
assert compareListOfLists(s.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]),
                                     [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]])