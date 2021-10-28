from typing import List
from colorama import init, Fore
init()

def highlight(lst, l=0, r=None):
    if l == 0 and r is None:
        return f"{Fore.CYAN}{lst}{Fore.RESET}"

    s = ""
    for i, elem in enumerate(lst):
        if l <= i < r:
            s += f", {Fore.CYAN}{elem}{Fore.RESET}"
        else:
            s += f", {elem}"
    return "[" + s[2:] + "]"

def bsearch(intervals, value, start, end):
    while start <= end:
        mid = (start + end) // 2

        if value < intervals[mid][0]:
            end = mid - 1
        elif value > intervals[mid][0]:
            start = mid + 1
        else:
            return mid
    return start

def merge(a, b):
    return [min(a[0], b[0]), max(a[1],b[1])]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        index = bsearch(intervals, newInterval[0], 0, len(intervals)-1)
        # print(f"searching for '{newInterval[0]}', best location at {index}, values:{intervals[index] if index < len(intervals) else None}, inserting {newInterval}")

        l = r = index
        while l-1 >= 0 and intervals[l-1][1] >= newInterval[0]:
            l -= 1
        while r < len(intervals) and intervals[r][0] <= newInterval[1]:
            r += 1

        middle = intervals[l:r]
        squash = newInterval
        if middle:
            tmp = merge(middle[0], middle[~0])
            squash = merge(newInterval, tmp)

        result = intervals[:l] + [squash] + intervals[r:]
        # print(f"merge {highlight(intervals, l, r)} with {highlight(newInterval)} into {highlight(squash)} and return {highlight(result,l,l+1)}")
        return result

# test bsearch
lst = [[i, i+1] for i in range(16, 128, 8)]
for i in range(0, 128, 2):
    index = bsearch(lst, i, 0, len(lst) - 1)
    # print(f"searching for {i}, best location at {index}, values:{lst[index] if index < len(lst) else None}")
    if index < len(lst):
        assert i <= lst[index][0]
    else:
        assert i >= lst[-1][0]

# test solution
s = Solution()
assert s.insert([], [5,7]) == [[5,7]]
assert s.insert([[1,2]], [1,2]) == [[1,2]]
assert s.insert([[1,5]], [2,3]) == [[1,5]]
assert s.insert([[2,3]], [1,5]) == [[1,5]]
assert s.insert([[1,5]], [2,7]) == [[1,7]]
assert s.insert([[2,7]], [1,5]) == [[1,7]]
assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [1,10]) == [[1,10]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [0,11]) == [[0,11]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [5,10]) == [[1,2],[3,4],[5,10]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [5,11]) == [[1,2],[3,4],[5,11]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [1,6]) == [[1,6],[7,8],[9,10]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [0,6]) == [[0,6],[7,8],[9,10]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [5,6]) == [[1,2],[3,4],[5,6],[7,8],[9,10]]
assert s.insert([[1,2],[3,4],[5,6],[7,8],[9,10]], [3,8]) == [[1,2],[3,8],[9,10]]
