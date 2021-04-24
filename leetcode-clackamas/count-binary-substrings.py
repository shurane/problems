class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # influenced by https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/
        # basically count the contiguous zeroes and ones.
        # When s[i] flips between zero and one, increment the count by the min run of zeroes followed by ones or vice-versa
        left = 0
        right = 1
        count = 0

        for i in range(1, len(s)):
            # print(i, left, right)
            if s[i-1] == s[i]:
                right += 1
            else:
                count += min(left, right)
                left = right
                right = 1

        count += min(left, right)

        return count

    def countBinarySubstrings2(self, s: str) -> int:
        # I'm treating this as growing the string from the middle, kind of like finding valid parantheses
        count = 0
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            lc = s[l]
            rc = s[r]
            while l >= 0 and r < len(s):
                if s[l] == lc and s[r] == rc and s[l] != s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

        return count

s = Solution()
assert s.countBinarySubstrings("10") == 1
assert s.countBinarySubstrings("101") == 2
assert s.countBinarySubstrings("010") == 2
assert s.countBinarySubstrings("1100") == 2
assert s.countBinarySubstrings("0011") == 2
assert s.countBinarySubstrings("10101") == 4
assert s.countBinarySubstrings("00110011") == 6