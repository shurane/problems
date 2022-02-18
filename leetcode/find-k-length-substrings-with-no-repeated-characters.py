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

s = Solution()
assert s.numKLenSubstrNoRepeats("abcdef", 1) == 6
assert s.numKLenSubstrNoRepeats("abcdef", 2) == 5
assert s.numKLenSubstrNoRepeats("aabbccddeeff", 2) == 5
assert s.numKLenSubstrNoRepeats("zaabbccddeeffg", 2) == 7
assert s.numKLenSubstrNoRepeats("havefunonleetcode", 5) == 6
assert s.numKLenSubstrNoRepeats("home", 5) == 0
