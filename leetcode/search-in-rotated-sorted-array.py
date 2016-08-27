# import blessings
# term = blessings.Terminal()

# def colorized_array(arr, begin, mid, end):
    # result = ""
    # space = " "
    # for i in range(len(arr)):
        # if i == len(arr) - 1:
            # space = ""
        
        # if i == begin:
            # result += term.red(str(arr[i])) + space
        # elif i == end:
            # result += term.blue(str(arr[i])) + space
        # # sometimes mid might overlap with begin or end
        # elif i == mid:
            # result += term.green(str(arr[i])) + space
        # else:
            # result += str(arr[i]) + space
    # return result

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = begin + (end - begin)/2

            # carr = colorized_array(nums, begin, mid, end)
            # print begin, mid, end, "target:{}, nums:{}".format(target, carr)

            if nums[mid] == target:
                return mid
            elif nums[begin] <= nums[mid]: # left half is sorted
                if nums[begin] <= target < nums[mid]: # search inside sorted left half
                    end = mid - 1
                else: # search right half
                    begin = mid + 1
            else: # right half is sorted
                if nums[mid] < target <= nums[end]: # search inside sorted right half
                    begin = mid + 1
                else: # search left half
                    end = mid - 1
        return -1

# s = Solution()
# a1 = [0,1,2,3,4,5,6,7,8,9]
# a2 = [4,5,6,7,8,9,0,1,2,3]

# print s.search(a1, 0)
# print s.search(a1, 3)
# print s.search(a1, 5)
# print s.search(a1, 7)
# print s.search(a1, 9)

# print s.search(a2, 0)
# print s.search(a2, 3)
# print s.search(a2, 5)
# print s.search(a2, 7)
# print s.search(a2, 9)

# print s.search([1, 3], 3)
# print s.search([4,5,6,7,8,1,2,3], 8)
