from typing import List
from heapq import heappop, heappush

class Solution:
    # https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        q = []
        start = 0
        for t, end in sorted(courses, key= lambda c: c[1]):
            start += t
            heappush(q, -t)
            while start > end:
                start += heappop(q)

        print(len(q), q)
        return len(q)

s = Solution()

assert s.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]) == 3
assert s.scheduleCourse([[1,2]]) == 1
assert s.scheduleCourse([[3,2],[4,3]]) == 0