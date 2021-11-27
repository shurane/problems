class Solution:
    # def __init__(self):
        # prealloc array up to 10,000
        # self.climbStairs(10000)

    def climbStairs(self, n: int):
        length = max(n+1, 3) # at least [0, 1, 2], since I'm doing 1-based indexing
        if not hasattr(self, 'arr'):
            # print "creating memoized arr of length {}".format(length)
            self.arr = [0 for i in range(length)]
            self.arr[1] = 1 #(1)
            self.arr[2] = 2 #(1,1) or (2)
            for i in range(3,length):
                self.arr[i] = self.arr[i-1] + self.arr[i-2]

        oldlength = len(self.arr)

        if oldlength < length:
            # print "extending... from {} to {}".format(oldlength, length)
            self.arr.extend([0 for i in range(length - oldlength)])
            for i in range(oldlength, length):
                self.arr[i] = self.arr[i-1] + self.arr[i-2]

        return self.arr[n]

    def climbStairsRedo1(self, n: int) -> int:
        # O(n) time, O(n) space
        if n == 1:
            return 1

        waysToClimb = [None] * (n + 1)
        waysToClimb[0] = 1
        waysToClimb[1] = 1

        for i in range(2, n + 1):
            waysToClimb[i] = waysToClimb[i-1] + waysToClimb[i-2]
        return waysToClimb[n]

    # from discussion, "basically it's a fibonacci" https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
    # didn't realize that. Makes sense. I guess I can start with (0, 1), (1, 1), or even (1, 2) for this.
    def climbStairsRedo2(self, n: int) -> int:
        # O(n) time, O(1) space
        if n == 1:
            return 1

        prev2 = 1
        prev1 = 1

        for _ in range(2, n + 1):
            succ = prev2 + prev1
            prev2 = prev1
            prev1 = succ
        return succ

    # done on 2021/11/26 with Rajib
    def climbStairsRedo3(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1
        curr = 2
        for i in range(2, n):
            temp = prev + curr
            prev = curr
            curr = temp

        return curr

s = Solution()

assert s.climbStairsRedo3(1) == 1
assert s.climbStairsRedo3(2) == 2
assert s.climbStairsRedo3(3) == 3
assert s.climbStairsRedo3(4) == 5
assert s.climbStairsRedo3(5) == 8
assert s.climbStairsRedo3(6) == 13
assert s.climbStairsRedo3(10) == 89
assert s.climbStairsRedo3(20) == 10946
assert s.climbStairsRedo3(50) == 20365011074
