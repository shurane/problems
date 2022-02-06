from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = prev = 0
        n = len(nums)

        while i < n:
            if i+1 < n and nums[i] == nums[i+1]:
                # keep a single duplicate
                end = i + 2
                while end < n and nums[i] == nums[end]:
                    end += 1

                nums[prev] = nums[i]
                nums[prev+1] = nums[i+1]
                prev += 2
                i = end
            else:
                nums[prev] = nums[i]
                prev += 1
                i += 1

        # # clear out the rest of the values for debugging
        # for j in range(prev, n):
        #     nums[j] = None
        # print(nums)

        return prev

s = Solution()
testcases = [[[0], [0]],
             [[0]*100, [0,0]],
             [[0]*100 + [1], [0,0,1]],
             [[0]*100 + [1] + [2] * 100, [0,0,1,2,2]],
             [[0,1,2,3,4], [0,1,2,3,4]],
             [[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5], [1,2,2,3,3,4,4,5,5]],
             [[1,1,1,1,1,2,2,2,2,3,3,3,4,4,5], [1,1,2,2,3,3,4,4,5]],
             [[0,0,1,1,2,2,3,3,4,4], [0,0,1,1,2,2,3,3,4,4]],
             [[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4], [0,0,1,1,2,2,3,3,4,4]],

             [[1,1,1,2,2,3], [1,1,2,2,3]],
             [[0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3]]]

for test, expected in testcases:
    k = s.removeDuplicates(test)
    assert test[:k] == expected