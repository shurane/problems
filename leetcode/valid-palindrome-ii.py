class Solution:
    def validPalindromeRecursive(self, s: str, deleted=False) -> bool:
        # this is correct, but slow and exceeds recursion depth on longstr
        # print(s, deleted)
        if len(s) <= 1:
            return True

        if s[0] == s[-1]:
            return self.validPalindromeRecursive(s[1:-1], deleted)
        elif s[0] != s[-1] and not deleted:
            return self.validPalindromeRecursive(s[1:], True) or self.validPalindromeRecursive(s[:-1], True)
        else:
            return False

    def validPalindrome(self, s: str, deleted=False) -> bool:
        # print(s, deleted)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j] and not deleted:
                return self.validPalindrome(s[i+1:j+1], True) or self.validPalindrome(s[i:j], True)
            else:
                return False
        return True


s = Solution()

assert s.validPalindrome("") == True
assert s.validPalindrome("a") == True
assert s.validPalindrome("aa") == True
assert s.validPalindrome("ab") == True
assert s.validPalindrome("aba") == True
assert s.validPalindrome("abc") == False
assert s.validPalindrome("abca") == True
assert s.validPalindrome("abbadabbad") == True
assert s.validPalindrome("dabbadabba") == True
assert s.validPalindrome("abcddcbaz") == True
assert s.validPalindrome("zabcddcba") == True
assert s.validPalindrome("abczddcbaz") == False

longstr = ""
with open("valid-palindrome-ii-long.txt") as f:
    longstr = f.read()

assert s.validPalindrome(longstr) == True