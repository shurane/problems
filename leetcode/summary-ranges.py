from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pairs = []
        i = 0
        while i < len(nums):
            begin = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
            end = nums[i]

            if begin != end:
                pairs.append(f"{begin}->{end}")
            else:
                pairs.append(str(begin))
            i += 1

        return pairs

s = Solution()
assert s.summaryRanges([]) == []
assert s.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert s.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
assert s.summaryRanges([0,1,2,3,4,5,6,7,8,9]) == ["0->9"]
assert s.summaryRanges([i*2 for i in range(50)]) == [str(i*2) for i in range(50)]
