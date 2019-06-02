from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] > 9:
            digits[i] = digits[i] % 10
            if i > 0:
                digits[i-1] += 1
            else:   
                digits.insert(0, 1)
            i -= 1

        return digits

s = Solution()
assert s.plusOne([0]) == [1]
assert s.plusOne([9]) == [1,0]
assert s.plusOne([9,9,9,9]) == [1,0,0,0,0]
assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]