from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        s = dict()
        for elem in arr:
            if elem not in s:
                s[elem] = 0
            s[elem] += 1

        counts = sorted(s.values(), reverse=True)
        total = 0
        i = 0
        l = len(arr) // 2
        while total < l and i < len(counts):
            total += counts[i]
            i += 1

        # print(counts, total, l, i)

        return i


s = Solution()
assert s.minSetSize([1,9]) == 1
assert s.minSetSize([1000,1000,3,7]) == 1
assert s.minSetSize([1000,2,3,7]) == 2
assert s.minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2
assert s.minSetSize([7,7,7,7,7,7]) == 1
assert s.minSetSize([1,2,3,4,5,6,7,8,9,10]) == 5
assert s.minSetSize([1,1,3,4,5,6,7,8,9,10]) == 4
assert s.minSetSize([1,1,1,4,5,6,7,8,9,10]) == 3
assert s.minSetSize([1,1,1,1,5,6,7,8,9,10]) == 2
assert s.minSetSize([1,1,1,1,1,6,7,8,9,10]) == 1

assert s.minSetSize([1,1,2,2,5,6,7,8,9,10]) == 3
assert s.minSetSize([1,1,2,2,2,6,7,8,9,10]) == 2