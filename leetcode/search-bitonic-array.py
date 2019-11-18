
# from educative.io Grokking the Coding Interview: Patterns for Coding Questions

class Solution:
    def searchBitonicArray(self, arr, value):
        peak = findBitonicPeak2(arr)
        # print("peak", peak)

        left = binarySearch(arr, 0, peak, value)
        # print("left", left)

        if left != -1:
            return left
        else:
            return binarySearch(arr, peak, len(arr) - 1, value)

def binarySearch(arr, lo, hi, value):
    # use direction as a way to indicate if the array is increasing or decreasing
    direction = 1
    if arr[lo] > arr[hi]:
        direction = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        dv, dam = direction * value, direction * arr[mid]
        if dv < dam :
            hi = mid - 1
        elif dv > dam:
            lo = mid + 1
        else:
            return mid

    return -1

# def findBitonicPeak(arr):
#     lo = 0
#     hi = len(arr) - 1

#     if len(arr) == 0:
#         return None
#     elif len(arr) == 1:
#         return 0

#     while lo < hi:
#         mid = (lo + hi) // 2
#         if arr[mid - 1] > arr[mid]:
#             hi = mid - 1
#         elif arr[mid + 1] > arr[mid]:
#             lo = mid + 1
#         else:
#             return mid

def findBitonicPeak2(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        # if arr[mid] < arr[mid + 1]:
        #     lo = mid + 1
        # else:
        #     hi = mid

        if arr[mid] > arr[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return lo

s = Solution()

assert findBitonicPeak2([0]) == 0
assert findBitonicPeak2([0, 1, 2, 3, 4, 5]) == 5
assert findBitonicPeak2([10, 9, 8]) == 0
assert findBitonicPeak2([1, 3, 8, 4, 3]) == 2
assert findBitonicPeak2([1,2,3,15,8,7,6,5,4,3,2,1,0,-1]) == 3

assert s.searchBitonicArray([0, 1, 2, 3, 4, 5], 3) == 3
assert s.searchBitonicArray([10, 9, 8], 10) == 0
assert s.searchBitonicArray([1, 3, 8, 4, 3], 10) == -1
assert s.searchBitonicArray([1, 3, 8, 4, 3], 4) == 3
assert s.searchBitonicArray([3, 8, 3, 1], 8) == 1
assert s.searchBitonicArray([1, 3, 8, 12], 12) == 3