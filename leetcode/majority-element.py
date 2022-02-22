from typing import List
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        best = nums[0]
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
            if counts[n] > counts[best]:
                best = n
        return best

    # https://leetcode.com/problems/majority-element/solution/
    # What is the Boyer-Moore Voting Algorithm? Very simple looking.
    # But how do you prove that it is true?
    def majorityElementBoyerMoore(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0: candidate = num

            if num == candidate: count += 1
            else: count -= 1

        return candidate

s = Solution()
assert s.majorityElement([3,2,3]) == 3
assert s.majorityElement([2,2,1,1,1,2,2]) == 2
assert s.majorityElementBoyerMoore([3,2,3]) == 3
assert s.majorityElementBoyerMoore([2,2,1,1,1,2,2]) == 2

l1 = [2 for _ in range(50)] + [3 for _ in range(49)]
l2 = [2 for _ in range(50)] + [3 for _ in range(51)]
random.shuffle(l1)
random.shuffle(l2)

assert s.majorityElement(l1) == 2
assert s.majorityElement(l2) == 3
assert s.majorityElementBoyerMoore(l1) == 2
assert s.majorityElementBoyerMoore(l2) == 3
