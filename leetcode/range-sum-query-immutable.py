import blessings
term = blessings.Terminal()

def colorized(lst, yellows=[]):
    result = "["
    delim = ", "
    for i in range(len(lst)):
        if i == len(lst) - 1:
            delim = ""

        v = "{: 3d}".format(lst[i])

        if i in yellows:
            result += term.yellow(v) + delim
        else:
            result +=             v  + delim

    result += "]"
    return result

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # make an n by n grid to query (i,j)
        n = len(nums)
        self.sumranges = [[0 for j in xrange(n)] for i in xrange(n)]

        if not nums:
            return

        self.sumranges[0][0] = nums[0]

        i = 0
        while i < len(nums):
            self.sumranges[i][i] = nums[i]
            j = i+1
            while j < len(nums):
                self.sumranges[i][j] = self.sumranges[i][j-1] + nums[j]
                j += 1
            i += 1

        for i in range(n):
            print colorized(self.sumranges[i], yellows = range(i,n))
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        # SR(i,j) = SR(i,j-1) + A[j]
        # SR(0,0) = 0
        # SR(i,i) = A[i]

        return self.sumranges[i][j]
        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
print numArray.sumRange(0, 5)
