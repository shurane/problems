from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pdict = {}
        for letter in p:
            if letter not in pdict:
                pdict[letter] = 0
            pdict[letter] += 1

        scount = 0
        sdict = {}
        results = []

        for letter in s[:k]:
            if letter not in sdict:
                sdict[letter] = 0
            sdict[letter] += 1
            if letter in pdict and sdict[letter] <= pdict[letter]:
                scount += 1

        if scount == k:
            # print("match", s[:k])
            results.append(0)

        for i in range(k, len(s)):
            letter = s[i]
            if letter not in sdict: sdict[letter] = 0

            # evict s[i-k] from the sliding window
            evictLetter = s[i-k]
            sdict[evictLetter] -= 1
            if evictLetter in pdict and sdict[evictLetter] < pdict[evictLetter]:
                scount -= 1

            # add s[i] to the sliding window
            sdict[letter] += 1
            if letter in pdict and sdict[letter] <= pdict[letter]:
                scount += 1

            ## this print statement is way too confusing to print the current window
            # print(i, s[i-k+1:i+1], letter, scount, sdict)

            if scount == k:
                # print("match", i-k+1, sdict)
                results.append(i-k+1)

        return results

s = Solution()

assert s.findAnagrams("cbaebabacd", "abc") == [0,6]
assert s.findAnagrams("abab", "ab") == [0,1,2]
assert s.findAnagrams("abc", "abcd") == []
