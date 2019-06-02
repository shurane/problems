class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or s.isspace():
            return 0
        return len(s.split()[-1])

s = Solution()

assert s.lengthOfLastWord("") == 0
assert s.lengthOfLastWord("     ") == 0
assert s.lengthOfLastWord("     wow") == 3
assert s.lengthOfLastWord("oh     wow") == 3
assert s.lengthOfLastWord("Hello World") == 5