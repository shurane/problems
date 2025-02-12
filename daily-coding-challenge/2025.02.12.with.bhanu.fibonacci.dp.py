

def fib(n: int, indent: int = 0) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    val = fib(n-1, indent+2) + fib(n-2, indent+2)
    print(" " * indent, "n:", n, "val:", val)

    return val

def fib_topdown_dp(n:int) -> int:
    dp = [-1 for _ in range(n+1)]

    def helper(i: int, indent=0) -> int:
        if i == 0:
            return 0
        elif i == 1 or i == 2:
            return 1
        elif dp[i] != -1:
            return dp[i]

        dp[i] = helper(i-1, indent+2) + helper(i-2, indent+2)
        print(" " * indent, f"helper({i}): {dp[i]}")

        return dp[i]

    print(f"fib_topdown_dp({n}) begin")
    print(f"fib_topdown_dp({n}) end", helper(n))
    return helper(n)

def fib_bottomup_dp(n: int) -> int:
    dp = [0, 1]

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    print("fib_bottomup_dp:", dp, dp[n])
    return dp[n]


def fib_bottomup_dp_spaceoptimized(n: int) -> int:
    if n <= 1:
        return n

    dp = [0, 1]

    print(f"fib_bottomup_dp_spaceoptimized({n})")
    for i in range(2, n+1):
        #  0  1  2  3  4  5  6   7   8   9  10      index
        # [0, 1] ->      [5, 8] -> [21, 34] -> ...  only care about last 2 values
        # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] fib(index)

        dp2 = dp[0] + dp[1]
        # print("i:", i, "previous fib nums:", dp, "current:", dp2)
        dp = [dp[1], dp2]

    return dp[1]


# https://r-knott.surrey.ac.uk/fibonacci/fibtable.html
f = fib_bottomup_dp_spaceoptimized
# assert(f(0) == 0)
# assert(f(1) == 1)
# assert(f(5) == 5)
# assert(f(10) == 55)
# assert(f(20) == 6765)
# assert(f(30) == 832040)
# assert(f(50) == 12586269025)
assert(f(100) == 354224848179261915075)