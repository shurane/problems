# from colorama import init, Fore, Back, Style
# init()

class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            print(lo, mid, hi)
            if target < nums[mid] and target >= nums[lo]:
                hi = mid - 1
            elif target < nums[mid] and target <= nums[lo]:
                lo = mid + 1
            elif target > nums[mid]:
                if target <= nums[hi]:
                    # sorted regularly, go right
                    lo = mid + 1
                elif target >= nums[lo] and target >= nums[hi]:
                    # break is on the right, go right
                    lo = mid + 1
                elif target <= nums[lo] and target >= nums[hi]:
                    # go left, but why?
                    hi = mid - 1
            # elif target > nums[mid] and target <= nums[hi]:
            #     lo = mid + 1
            # elif target > nums[mid] and target >= nums[hi]:
            #     hi = mid - 1
            else:
                return mid
        return -1

    def search2(self, nums, target):
        import time
        # find break
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            time.sleep(0.2)
            mid = (lo + hi) // 2
            print(lo, mid, hi)
            # print(f"{Fore.RED}{nums[lo]}{Style.RESET_ALL}, {str(nums[lo:mid])[1:-1]} {str(nums[mid+1:hi])[1:-1]} {Fore.YELLOW}{nums[hi]}{Style.RESET_ALL}")
            if nums[lo] > nums[mid] and nums[mid] < nums[hi]:
                # go left
                hi = mid - 1
            elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                # go right
                lo = mid + 1
        print("after", lo, mid, hi)
        return mid
            

            

s = Solution()

# assert s.search([0], 0) == 0
# assert s.search([0], 1) == -1
# assert s.search([0,1,2,3,4,-1], 1) == 1
# assert s.search([0,1,2,3,4,-1], -1) == 5
# assert s.search(list(range(1023)) + [-1], -1) == 1023
# assert s.search([4,5,6,7,0,1,2], 0) == 4
# assert s.search([4,5,6,7,8,1,2,3], 8) == 4
# 35 min extra

assert s.search2([4,5,6,7,8,1,2,3], 8) == 5
assert s.search2([0,1,2,3,4,-1], 1) == 5

"""
0 1 2 3 4 5 6 7
---------------
4 5 6 7 8 1 2 3

target = 8

lo  mid hi
0   3   7   4   7   3
0   1   2   
0   0   0

"""