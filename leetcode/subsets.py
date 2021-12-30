from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        combinations = 2 ** n
        subsets = []

        # this is slow. Possibly because bit manipulation is slow in Python. Should look at other solutions
        for i in range(combinations):
            lst = []
            for index in range(n):
                # print(i, index, 2 ** index)
                if i & (2 ** index):
                    lst.append(nums[index])
            subsets.append(lst)

        return subsets

s = Solution()
assert s.subsets([]) == [[]]
assert s.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert s.subsets([1,2,3,4]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]
