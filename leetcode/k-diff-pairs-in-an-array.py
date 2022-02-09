from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        history = set()
        pairs = set()
        # print("k:", k, "nums:", nums)
        for num in nums:
            numkplus = num + k
            numkminus = num - k
            if numkplus in history and (num, numkplus) not in pairs:
                pairs.add((num, numkplus))
            if numkminus in history and (numkminus, num) not in pairs:
                pairs.add((numkminus, num))
            history.add(num)
            # print(f"num: {num:3}, numk-: {numkminus:3}, numk+: {numkplus:3}, history: {history}, pairs: {pairs}")
        return len(pairs)

s = Solution()

assert s.findPairs([3,1,4,1,5], 2) == 2
assert s.findPairs([1,2,3,4,5], 1) == 4
assert s.findPairs([1,2,3,4,5], 5) == 0
assert s.findPairs([1,2,3,4,5,1,2,3,4,5], 1) == 4
assert s.findPairs([1,3,1,5,4], 0) == 1

assert s.findPairs([1,2,4,4,3,3,0,9,2,3], 3) == 2
assert s.findPairs([1,2,3], 1) == 2
assert s.findPairs([-1,-2,-3], 1) == 2

assert s.findPairs([-5,5], 5) == 0
assert s.findPairs([-10,-5,5,10], 5) == 2
assert s.findPairs([-10,-5,0], 5) == 2
assert s.findPairs([-5,0,5], 5) == 2
assert s.findPairs([0,5,10], 5) == 2