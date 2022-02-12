class Solution:
    # https://leetcode.com/problems/one-edit-distance/discuss/50190/JavaPython-two-pointer-solution
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if abs(m - n) > 1:
            return False

        i = 0
        j = 0
        k = min(m, n)
        # comparing left side of the string
        while i < k and s[i] == t[i]:
            i += 1
        # comparing right side of the string
        while j < k - i and s[m - 1 - j] == t[n - 1 - j]:
            j += 1

        return max(m, n) - 1 == i + j

s = Solution()
assert s.isOneEditDistance("", "") == False
assert s.isOneEditDistance("ab", "acb") == True
assert s.isOneEditDistance("ab", "abb") == True
assert s.isOneEditDistance("ab", "abbbbbbb") == False
assert s.isOneEditDistance("aba", "bab") == False # edit distance is 2
assert s.isOneEditDistance("abcc", "accc") == True