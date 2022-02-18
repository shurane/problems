from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        m = defaultdict(int)
        match = 0
        results = 0

        for i in range(len(s)+1):
            if i-k >= 0:
                # print(i-k, i, match, k, match == k, s[i-k:i])

                if match == k:
                    # print("matched", s[i-k:i])
                    results += 1

                prevLetter = s[i-k]

                m[prevLetter] -= 1

                # k=4, 'aabc', > 'abcd', single 'a' now (2 to 1)
                if m[prevLetter] == 1:
                    match += 1
                # k=4, 'abcd' > 'bcde', 'a' gets evicted (1 to 0)
                elif m[prevLetter] == 0:
                    match -= 1

            if i < len(s):
                letter = s[i]
                m[letter] += 1

                if m[letter] == 1:
                    match += 1
                elif m[letter] == 2:
                    match -= 1

        return results

    # https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/1776611/Python-Sliding-windows-fun
    def numKLenSubstrNoRepeatsSimpler(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        dupes = 0

        for i in range(len(s)):
            count[s[i]] += 1
            if count[s[i]] == 2:
                dupes += 1

            if i-k>=0:
                count[s[i-k]] -= 1
                if count[s[i-k]] == 1:
                    dupes -= 1

            res += i-k+1>=0 and dupes == 0
        return res

s = Solution()

assert s.numKLenSubstrNoRepeats("abcdef", 1) == 6
assert s.numKLenSubstrNoRepeats("abcdef", 2) == 5
assert s.numKLenSubstrNoRepeats("aabbccddeeff", 2) == 5
assert s.numKLenSubstrNoRepeats("zaabbccddeeffg", 2) == 7
assert s.numKLenSubstrNoRepeats("havefunonleetcode", 5) == 6
assert s.numKLenSubstrNoRepeats("home", 5) == 0

assert s.numKLenSubstrNoRepeatsSimpler("abcdef", 1) == 6
assert s.numKLenSubstrNoRepeatsSimpler("abcdef", 2) == 5
assert s.numKLenSubstrNoRepeatsSimpler("aabbccddeeff", 2) == 5
assert s.numKLenSubstrNoRepeatsSimpler("zaabbccddeeffg", 2) == 7
assert s.numKLenSubstrNoRepeatsSimpler("havefunonleetcode", 5) == 6
assert s.numKLenSubstrNoRepeatsSimpler("home", 5) == 0
