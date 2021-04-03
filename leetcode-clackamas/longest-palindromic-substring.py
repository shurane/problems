class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSeen = ""
        center = 0
        while center < len(s):
            # even length
            l = center
            r = center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l:r]) > len(longestSeen):
                longestSeen = s[l:r]

            # odd length
            l = center - 1
            r = center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l:r]) > len(longestSeen):
                longestSeen = s[l:r]

            center += 1
        return longestSeen

def longestAroundCenter(s: str, l: int, r: int):
    pass

# def isPalindrome(s: str) -> bool:
#     # would this help in finding the "longest" palindrome? it ends up looping more times.
#     l, r = 0, len(s) - 1

#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

s = Solution()

print(s.longestPalindrome("a"))
print(s.longestPalindrome("aba"))
print(s.longestPalindrome("abba"))
# assert isPalindrome("a") == True
# assert isPalindrome("ab") == False
# assert isPalindrome("aba") == True
# assert isPalindrome("abba") == True
# assert isPalindrome("aaba") == False
# assert isPalindrome("abaa") == False
# assert s.longestPalindrome("a") == "a"
# assert s.longestPalindrome("ac") == "a"
# assert s.longestPalindrome("babad") == "bab"
# assert s.longestPalindrome("cbbd") == "bb"