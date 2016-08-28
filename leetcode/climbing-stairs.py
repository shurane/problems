class Solution(object):
    def __init__(self):
        # prealloc array up to 10,000
        self.climbStairs(10000)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = max(n+1, 3)
        if not hasattr(self, 'arr'):
            # print "creating memoized arr of length {}".format(length)
            self.arr = [0 for i in xrange(length)]
            self.arr[1] = 1 #(1)
            self.arr[2] = 2 #(1,1) or (2)
            for i in range(3,length):
                self.arr[i] = self.arr[i-1] + self.arr[i-2]

        oldlength = len(self.arr)

        if oldlength < length:
            # print "extending... from {} to {}".format(oldlength, length)
            self.arr.extend([0 for i in xrange(length - oldlength)])
            for i in range(oldlength, length):
                self.arr[i] = self.arr[i-1] + self.arr[i-2]

        return self.arr[n]

# s = Solution()

# print s.climbStairs(10)
# print s.climbStairs(4)
# print s.climbStairs(5)
# print s.climbStairs(20)
# print s.climbStairs(20)
