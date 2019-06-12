import re

class Solution:
    def isPalindrome2(self, s: str) -> bool:
        s = re.sub("\W", "", s).lower()

        if len(s) <= 1:
            return True

        i = 0
        while i <= len(s) // 2:
            if s[i] != s[-1 - i]:
                return False
            i += 1

        return True

    def isPalindrome(self, s: str) -> bool:
        # saw https://leetcode.com/problems/valid-palindrome/discuss/39982/Python-in-place-two-pointer-solution. and was inspired. pretty simple way without using regular expressions and lowering the whole string
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True