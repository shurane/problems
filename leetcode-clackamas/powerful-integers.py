from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        elems = set()
        i = 0
        while x ** i < bound:
            j = 0
            while x ** i + y ** j <= bound:
                elems.add(x ** i + y ** j)
                j += 1
                if y == 1: break
            i += 1

            if x == 1: break

        elems = sorted(elems)
        # print(x, y, bound, elems)
        return elems

s = Solution()
assert s.powerfulIntegers(1, 1, 1) == []
assert s.powerfulIntegers(1, 1, 10) == [2]
assert s.powerfulIntegers(2, 1, 10) == [2,3,5,9]
assert s.powerfulIntegers(1, 2, 10) == [2,3,5,9]
assert s.powerfulIntegers(2, 3, 10) == [2,3,4,5,7,9,10]
assert s.powerfulIntegers(3, 5, 15) == [2,4,6,8,10,14]