class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 1

        i = 0
        count = 0
        while i < len(s):
            # odd strings expand left and right by 1
            l = i
            r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                # print(f" odd {i:2}, {l:2}, {r:2}, {s[l:r+1]}")
                l -= 1
                r += 1
                count += 1

            # even strings expand left and right by 1
            l = i
            r = i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                # print(f"even {i:2}, {l:2}, {r:2}, {s[l:r+1]}")
                l -= 1
                r += 1
                count += 1

            i += 1

        # print(s, count)
        return count

# def isPalindrome(s: str) -> bool:
#     l = 0
#     r = len(s) - 1
#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

# assert isPalindrome("abcba")
# assert isPalindrome("abba")
# assert isPalindrome("abc") == False

s = Solution()
assert s.countSubstrings("") == 1
assert s.countSubstrings("a") == 1
assert s.countSubstrings("abc") == 3
assert s.countSubstrings("aaa") == 6
assert s.countSubstrings("abba") == 6
assert s.countSubstrings("abcdcba") == 10
assert s.countSubstrings("bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb") == 64
word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
assert s.countSubstrings(word) == 500500