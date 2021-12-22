from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    return mid
            return -1

        # TODO can I deduplicate leftSearch and rightSearch? it's basically the same code
        def leftSearch(lo, hi, target):
            while lo < hi:
                mid = (lo + hi) // 2
                if target == nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo

        def rightSearch(lo, hi, target):
            while lo < hi:
                mid = (lo + hi) // 2
                if target == nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        n = len(nums) - 1
        i = binarySearch(0, n, target)
        if i == -1:
            # print(-1, -1, "target", target)
            return [-1, -1]

        l = leftSearch(0, i, target)
        r = rightSearch(i, n, target)
        # shrink boundaries if l,r are off by one
        if nums[l] != target: l += 1
        if nums[r] != target: r -= 1
        # print(l, r, "target", target)
        return [l,r]

s = Solution()
assert s.searchRange([], 0) == [-1, -1]
assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert s.searchRange([5,7,7,8,8,10], 6) == [-1,-1]

l1 = [1] + [2] * 998 + [3]
l2 = [1] * 20 + [2] * 20 + [3] * 20
l3 = [1] * 50 + [2] * 10 + [3] * 70
assert s.searchRange(l1, 2) == [1, 998]
assert s.searchRange(l2, 2) == [20,39]
assert s.searchRange(l3, 2) == [50,59]

# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
BLACK   = "\u001b[30m"
RED     = "\u001b[31m"
GREEN   = "\u001b[32m"
YELLOW  = "\u001b[33m"
BLUE    = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN    = "\u001b[36m"
WHITE   = "\u001b[37m"
RESET   = "\u001b[0m"

def coloredlist(lst, target):
    s = "["
    for i, elem in enumerate(lst):
        if elem < target:
            s += YELLOW
        elif elem > target:
            s += MAGENTA
        else:
            s += GREEN
        s += f"{elem}{RESET}"

        if i != len(lst) - 1:
            s += ", "
    s += " ]"
    return s

SIZE = 32

for i in range(SIZE + 1):
    for j in range(SIZE + 1 - i):
        left = [1] * j
        mid = [2] * i
        right = [3] * (SIZE - i - j)
        lst = left + mid + right
        print(coloredlist(lst, 2), len(lst))
        if len(mid) == 0:
            assert s.searchRange(lst, 2) == [-1, -1]
        else:
            assert s.searchRange(lst, 2) == [j, j + i - 1]
