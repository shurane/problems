from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # really slow solution. I may have to scan half the list before getting an answer. That's O(n)
        # What's a better approach? is there something to use the fact that the input array is sorted?
        # print(f"twoSum(numbers={numbers}, target={target})")
        i = 0
        while i < len(numbers) // 2 + 1:
            leftover = target - numbers[i]
            # print(f"twoSum(i={i}, leftover={leftover})")
            j = bsearch(numbers, leftover, i + 1, len(numbers) - 1)
            # print(f"twoSum(j={j})")
            if j > -1:
                return [i + 1, j + 1]
            i += 1

        return None

    def twoSumTwoPointers(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1, r+1]
        return None

def bsearch(numbers, goal, lo=None, hi=None):
    if lo == None:
        lo = 0
    if hi == None:
        hi = len(numbers) - 1

    # print(f"bsearch(goal={goal}, lo={lo}, hi={hi})")

    while lo <= hi:
        mid = (lo + hi) // 2
        # print(f"bsearch(mid={mid}, lo={lo}, hi={hi})")
        if goal < numbers[mid]:
            hi = mid - 1
        elif goal > numbers[mid]:
            lo = mid + 1
        else:
            return mid

    return -1

s = Solution()

# assert s.twoSum([2,7,11,15], 9) == [1,2]
# assert s.twoSum([2,3,4], 6) == [1,3]
# assert s.twoSum([5,25,75], 100) == [2, 3]
# assert s.twoSum([1,2,3,4,4,9,56,90], 8) == [4, 5]
# assert s.twoSum([1] + [2 for i in range(1000000)] + [5 for i in range(1000000)] + [19], 20) == [1, 2000002]

assert s.twoSumTwoPointers([2,7,11,15], 9) == [1,2]
assert s.twoSumTwoPointers([2,3,4], 6) == [1,3]
assert s.twoSumTwoPointers([5,25,75], 100) == [2, 3]
assert s.twoSumTwoPointers([1,2,3,4,4,9,56,90], 8) == [4, 5]
# assert s.twoSumTwoPointers([1] + [2 for i in range(1000000)] + [5 for i in range(1000000)] + [19], 20) == [1, 2000002]