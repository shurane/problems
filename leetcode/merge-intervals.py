from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        i = 1
        while i < len(intervals):
            left = intervals[i-1]
            right = intervals[i]

            # overlapping
            if left[1] >= right[0]:
                left[1] = max(left[1], right[1])
                intervals.pop(i)
            else:
                i += 1
        # print("intervals", intervals)
        return intervals

    def mergeNewList(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        results = [intervals[0]]

        for right in intervals[1:]:
            # overlapping with last value in results
            if results[-1][1] >= right[0]:
                results[-1][1] = max(results[-1][1], right[1])
            else:
                results.append(right)
        return results

s = Solution()

assert s.mergeNewList([[1,10],[2,9],[3,8],[4,7],[5,6]]) == [[1,10]]
assert s.mergeNewList([[1,6],[2,7],[3,8],[4,9],[5,10]]) == [[1,10]]
assert s.mergeNewList([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]) == [[1,10]]
assert s.mergeNewList([[1,2],[3,4],[5,6],[7,8],[9,10]]) == [[1,2],[3,4],[5,6],[7,8],[9,10]]
