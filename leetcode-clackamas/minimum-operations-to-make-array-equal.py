class Solution:
    def minOperationsIterative(self, n: int) -> int:
        result = 0
        for i in range(n // 2):
            result += (i * 2) + 1
            result += n % 2

        # arr = [(2 * i) + 1 for i in range(n)]
        # print(n, result, arr)

        return result

    def minOperations(self, n: int) -> int:
        # https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/1145082/Simple-O(1)-1-Liner-or-Easy-Solution-w-Explanation-or-Beats-100
        # look into arithmetic progression, should help for understanding how to simplify to this
        half = n // 2
        return (n - half) * half
        # even simpler solution
        # return n * n // 4

s = Solution()
assert s.minOperations(1) == 0
assert s.minOperations(2) == 1 # + 1
assert s.minOperations(3) == 2 # + 1
assert s.minOperations(4) == 4 # + 2
assert s.minOperations(5) == 6 # + 2
assert s.minOperations(6) == 9 # + 3
assert s.minOperations(7) == 12 # + 3
assert s.minOperations(8) == 16 # + 4
assert s.minOperations(9) == 20 # + 4
assert s.minOperations(15) == 56