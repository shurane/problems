class Solution:
    f = [0,1,1]

    def fib2(self, N: int) -> int:
        if N == 0:
            return 0
        if N <= 2:
            return 1

        a, b = 1, 1
        i = 2
        while i < N:
            a, b = b, a + b
            i += 1

        return b

    def fib(self, N: int) -> int:
        ff = self.__class__.f
        if N < len(ff):
            return ff[N]

        i = len(ff)
        while i <= N:
            ff.append(ff[-1] + ff[-2])
            i += 1

        return ff[N]


f = Solution()

assert f.fib(0) == 0
assert f.fib(1) == 1
assert f.fib(2) == 1
assert f.fib(3) == 2
assert f.fib(4) == 3
assert f.fib(5) == 5

# 5 minutes, took time to set up the memoization