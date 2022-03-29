from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target or nums[lo] == target or nums[hi] == target:
                return True
            elif nums[lo] < nums[mid]:
                if nums[lo] < target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[lo]:
                if nums[mid] < target < nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1

        return False

    def searchSlow(self, nums: List[int], target: int) -> bool:
        lo = 0
        hi = len(nums) - 1
        pivot = 0
        mid = -1

        q = [(lo,hi)]
        while q:
            # print(q)
            nextq = []
            for l, h  in q:
                mid = (l + h) // 2
                if l >= h-1 and nums[l] > nums[h]:
                    pivot = h
                    continue
                if nums[l] <= nums[mid] and nums[mid] <= nums[h]:
                    continue
                if nums[l] > nums[mid]: nextq.append((l, mid))
                elif nums[h] < nums[mid]: nextq.append((mid, h))
            q = nextq

        if pivot == 0:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    pivot = i+1
                    break

        res = False
        if pivot > 0:
            res = bsearch(nums, 0, pivot, target)
            if res == -1:
                res = bsearch(nums, pivot, len(nums) - 1, target)
        else:
            res = bsearch(nums, 0, len(nums) - 1, target)

        return res != -1

def bsearch(lst: List[int], lo: int, hi: int, target: int) -> int:
    while lo <= hi:
        mid = (lo + hi) // 2

        if target < lst[mid]:
            hi = mid - 1
        elif target > lst[mid]:
            lo = mid + 1
        else:
            return mid

    return -1

s = Solution()

assert s.search([2,5,6,0,0,1,2], 0) == True
assert s.search([2,5,6,0,0,1,2], 3) == False
assert s.search([1,0,1,1,1], 0) == True

n = 32

l1 = [0 for _ in range(n)]
assert s.search(l1, 0) == True
assert s.search(l1, -1) == False
assert s.search(l1, 1) == False
assert s.searchSlow(l1, 0) == True
assert s.searchSlow(l1, -1) == False
assert s.searchSlow(l1, 1) == False

l2 = []
for i in range(n): l2.extend([i,i])

for i in range(n*2):
    newl = l2[i:] + l2[:i]

    assert s.search(newl, -1) == False
    assert s.search(newl, n) == False
    assert s.searchSlow(newl, -1) == False
    assert s.searchSlow(newl, n) == False
    for target in range(n):
        # print(target, newl)
        assert s.search(newl, target) == True
        assert s.searchSlow(newl, target) == True

l3 = [0]
for i in range(n): l3.extend([i] * i)

for i in range(len(l3)):
    newl = l3[i:] + l3[:i]
    assert s.search(newl, -1) == False
    assert s.search(newl, n) == False
    assert s.searchSlow(newl, -1) == False
    assert s.searchSlow(newl, n) == False
    for target in range(n):
        # print(target, newl)
        assert s.search(newl, target) == True
        assert s.searchSlow(newl, target) == True

for i in range(n):
    newl = [1] * n
    newl[i] = 0
    assert s.search(newl, 0) == True
    assert s.searchSlow(newl, 0) == True

for i in range(n):
    newl = [0] * n
    newl[i] = 1
    assert s.search(newl, 1) == True
    assert s.searchSlow(newl, 1) == True
