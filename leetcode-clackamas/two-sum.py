class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for index, num in enumerate(nums):
            if (target - num) in hash:
                return [hash[target-num], index]
            else:
                hash[num] = index

        raise Exception

