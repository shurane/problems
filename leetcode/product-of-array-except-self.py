from typing import List

class Solution:
    def productExceptSelfSlow(self, nums: List[int]) -> List[int]:
        results = [1 for num in nums]
        lefts   = [1 for num in nums]
        rights  = [1 for num in nums]

        i = 1
        j = len(nums) - 2
        lefts[0] = nums[0]
        rights[-1] = nums[-1]

        while i < len(nums) - 1:
            lefts[i] = lefts[i-1] * nums[i]
            rights[j] = rights[j+1] * nums[j]

            i += 1
            j -= 1

        results[0] = rights[1]
        results[-1] = lefts[-2]
        k = 1
        while k < len(nums) - 1:
            results[k] = lefts[k-1] * rights[k + 1]

            k += 1

        # print(lefts)
        # print(rights)
        # print(results)

        return results


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ok, this is O(1) per the solution, but... could be done more neatly
        results = [1 for num in nums]

        results[0] = nums[0]
        i = 1
        while i < len(nums):
            results[i] = results[i-1] * nums[i]
            i += 1
        print("before:", results)

        rolling = nums[-1]
        results[-1] = results[-2]
        j = len(nums) - 2

        while j > 0:
            results[j] = results[j-1] * rolling
            rolling = rolling * nums[j]
            j -= 1

        results[0] = rolling

        print("after :", results)
        return results

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([1,2]) == [2,1]
assert s.productExceptSelf([20,13]) == [13,20]