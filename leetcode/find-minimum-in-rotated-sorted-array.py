# import blessings
# term = blessings.Terminal()

# def colorized_array(arr, begin, mid, end):
    # result = ""
    # space = " "
    # for i in range(len(arr)):
        # if i == len(arr) - 1:
            # space = ""
        
        # r = "{: 3d}".format(arr[i])
        # if i == begin:
            # result += term.red(r) + space
        # elif i == end:
            # result += term.blue(r) + space
        # # sometimes mid might overlap with begin or end
        # elif i == mid:
            # result += term.green(r) + space
        # else:
            # result += str(r) + space
    # return result

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # isn't this the equivalent of finding the pivot and comparing that to
        # the leftmost element?
        begin = 0
        end = len(nums) - 1

        lowest = nums[begin]

        while begin <= end:
            mid = begin + (end - begin)/2

            # carr = colorized_array(nums, begin, mid, end)
            # print "{: 3d}".format(begin), "{: 3d}".format(mid), "{: 3d}".format(end), 
            # print "lowest:{: 3d}, nums:{}".format(lowest, carr)

            lowest = min(lowest, nums[begin], nums[mid], nums[end])

            # go down the half that isn't sorted
            if nums[begin] > nums[mid]:
                # left half unsorted
                end = mid - 1
            else:
                # right half unsorted
                begin = mid + 1
        return lowest


s = Solution()
a1 = range(16)

for i in range(len(a1)):
    # rotate the array around... should always return 0
    newA = a1[i:] + a1[:i]
    print s.findMin(newA)
