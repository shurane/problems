class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0

        # Sieve of Eratosthenes. Some optimizations based on reading solutions online
        s = [1 for i in range(n)]
        s[0] = s[1] = 0
        for i in range(4, n, 2): s[i] = 0 # mark off all multiples of 2
        for i in range(3, int(n**0.5) + 1, 2):
            if s[i] == 0: continue

            for j in range(i**2, n, i):
                s[j] = 0

        return sum(s)

s = Solution()
assert s.countPrimes(0) == 0
assert s.countPrimes(1) == 0
assert s.countPrimes(2) == 0
assert s.countPrimes(3) == 1
assert s.countPrimes(10) == 4
# https://primes.utm.edu/howmany.html
assert s.countPrimes(10 ** 4) == 1229
assert s.countPrimes(10 ** 6) == 78498
assert s.countPrimes(4 * 10 ** 6) == 283146
# assert s.countPrimes(10 ** 7) == 664579

