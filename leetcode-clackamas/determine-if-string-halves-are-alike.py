class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left, right = 0, 0

        for c in s[:len(s)//2]:
            if c in "aeiouAEIOU": left += 1
        for c in s[len(s)//2:]:
            if c in "aeiouAEIOU": right += 1

        return left == right

s = Solution()

assert s.halvesAreAlike("book") == True
assert s.halvesAreAlike("textbook") == False
assert s.halvesAreAlike("MerryChristmas") == False
assert s.halvesAreAlike("AbCdEfGh") == True