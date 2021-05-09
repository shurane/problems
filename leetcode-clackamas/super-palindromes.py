import math

def base3(n: int, num: str = "") -> str:
    if not n: return num
    n, r = divmod(n, 3)
    return base3(n, str(r) + num)

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # https://leetcode.com/problems/super-palindromes/discuss/1197697/JS-Python-Java-C%2B%2B-or-Two-Fast-Mathematical-Solutions-w-Explanation

        l = int(left)
        r = int(right)

        palindromes = []
        # 3 isn't a digit that shows up in base 3 so check manually
        if l <= 9 <= r:
            palindromes.append((3,"10", 9))
        for i in range(1, 19684):
            num = base3(i)
            square = int(num) * int(num)

            if square >= r: break
            if num == num[::-1] and str(square) == str(square)[::-1] and l <= square:
                palindromes.append((i, num, square))

        for p in palindromes:
          print(p)
        return len(palindromes)

    def superpalindromesInRange2(self, left: str, right: str) -> int:
        # Original solution, but slow to iterate over an entire range.
        # Better to find a pattern between palindrome numbers and their palindrome squares
        lower = int(math.sqrt(int(left)))
        higher = int(math.sqrt(int(right)))
        # print(lower, higher)

        palindromes = []
        for i in range(lower, higher+1):
            square = i * i

            if str(i) == str(i)[::-1] and str(square) == str(square)[::-1]:
                palindromes.append((i, square))

        print(palindromes)
        return len(palindromes)

s = Solution()
assert s.superpalindromesInRange("4", "1000") == 4
assert s.superpalindromesInRange("375259531", "1265368034085") == 18