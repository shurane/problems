class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return

        n = len(nums)
        self.sumranges = [0 for i in nums]
        self.nums = nums

        self.sumranges[0] = nums[0]

        for i in xrange(1,n):
            self.sumranges[i] = self.sumranges[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        # the n-by-n grid was too much...
        # the problem here is the n by n grid... it's O(n^2) space
        # it chokes on an input of n=10,000
        # so... what to do?

        # there's a simpler recurrence relation that is linear

        # SR(i,j) = SR(i,j-1) + A[j]
        # SR(i,i) = A[i]


        return self.sumranges[j] - self.sumranges[i] + self.nums[i]



# nums = [-2, 0, 3, -5, 2, -1]
# numArray = NumArray(nums)
# assert numArray.sumRange(0, 2) == 1
# assert numArray.sumRange(2, 5) == -1
# assert numArray.sumRange(0, 5) == -3

n2 = NumArray([1000,2])
assert n2.sumRange(0,0) == 1000
assert n2.sumRange(0,1) == 1002
assert n2.sumRange(1,1) == 2

# n3 = NumArray([10,20,30,40,50])
# print n3.sumRange(0,0) # 10
# print n3.sumRange(0,1) # 10 + 20 == 30
# print n3.sumRange(0,2) # 10 + 20 + 30 == 60
# print n3.sumRange(0,3) # 10 + 20 + 30 + 40 == 100
# print n3.sumRange(0,4) # 10 + 20 + 30 + 40 + 50 == 150
# print n3.sumRange(1,1) # 20
# print n3.sumRange(1,2) # 20 + 30 == 50
# print n3.sumRange(1,3) # 20 + 30 + 40 == 90
# print n3.sumRange(1,4) # 20 + 30 + 40 + 50 == 140

