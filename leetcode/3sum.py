from collections import Counter

def flatten(lstoflsts):
    flat_list = []
    for sublist in lstoflsts:
        for item in sublist:
            flat_list.append(item)
    return flat_list

class Solution(object):
    def threeSumGeeksforGeeks(self, nums):
        # very clever... hats off
        # O(n^2)
        # https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
        # s = sorted(nums)
        d = Counter(nums)
        s2 = sorted(flatten([[k] * min(v, 2) for k, v in d.items()]))

        if d[0] >= 3:
            s2.insert(s2.index(0), 0)

        # print(len(s),len(s2))

        combinations = set()

        for i in range(len(s2) - 2):
            l = i + 1
            r = len(s2) - 1

            while l < r:
                amount = s2[i] + s2[l] + s2[r]
                if amount == 0:
                    combinations.add(tuple([s2[i], s2[l], s2[r]]))
                    l += 1
                elif amount < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(combo) for combo in sorted(combinations)]

    def threeSumSorted(self, nums):
        # O(n^2logn)
        sortedNums = sorted(nums)

        combinations = set()

        i = 0
        while i < len(sortedNums):
            j = 0
            while j < len(sortedNums):
                if i == j:
                    j += 1
                    continue
                total = sortedNums[i] + sortedNums[j]
                leftover = 0 - total

                matchIndex = self.binarySearch(sortedNums, leftover)

                if matchIndex > 0 and matchIndex != i and matchIndex != j:
                    combo = tuple(sorted([sortedNums[matchIndex], sortedNums[i], sortedNums[j]]))
                    combinations.add(combo)

                j += 1
            i += 1

        return [list(combo) for combo in sorted(combinations)]

    def binarySearch(self, lst, value):
        lo = 0
        hi = len(lst) - 1
        mid = int((lo + hi) / 2)

        while lo < mid and mid < hi:
            if value < lst[mid]:
                hi = mid
            elif lst[mid] < value:
                lo = mid
            else:
                return mid

            mid = int((lo + hi) / 2)
        
        return -1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(n) for iterating through the loop once
        # O(n) for each i by calling twoSum(0 - nums[i], nums[:i], nums[i+1:])
        # total runtime? O(n^2)

        i = 0
        combinations = set()
        while i < len(nums):
            target = 0 - nums[i]
            searchNums = nums[:i] + nums[i+1:]
            
            results = self.twoSum(searchNums, target)
            # print("threeSum", nums[i], results)
            # print(searchNums, target)

            for pair in results:
                combo = tuple(sorted([nums[i]] + pair))
                combinations.add(combo)

            i += 1

        return [list(combo) for combo in sorted(combinations)]

    def twoSum(self, nums, target):
        # O(n) to iterate over nums, and O(n) to construct the set
        # total runtime? O(n)
        visited = set()

        results = set()

        i = 0
        while i < len(nums):
            leftover = target - nums[i]

            if leftover in visited:
                results.add(tuple(sorted([nums[i], leftover])))

            visited.add(nums[i])

            i += 1

        if results:
            return [list(combo) for combo in results]
        return []
            

s = Solution()

# print(s.binarySearch(list(range(100)), 115))

# print(s.twoSum([2, 7, 11, 15], 9))
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSumGeeksforGeeks([-1, 0, 1, 2, -1, -4]))
# print(s.threeSumGeeksforGeeks([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

# https://pymotw.com/2/profile/
import random
import time
import profile
random.seed(0)
nums = [random.randint(-1000,1000) for i in range(1000)]
start = time.time()
profile.run("print(s.threeSumGeeksforGeeks(nums))")
stop = time.time()
elapsed = stop - start
print("elapsed", elapsed)

# output was [[-4,1,3],[-4,2,2],[-2,-2,4],[-4,-2,6],[-2,0,2]]
# expected was [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# [-4, 0, 4] is missing