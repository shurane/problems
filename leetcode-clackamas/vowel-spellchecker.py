from typing import List

def devowel(word: str):
    transformed = []
    for letter in word.lower():
        if letter in "aeiou":
            transformed.append("*")
        else:
            transformed.append(letter)
    return "".join(transformed)

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        s = set(wordlist)
        lowermap = dict()
        vowelmap = dict()

        for word in wordlist:
            wl = word.lower()
            if not wl in lowermap:
                lowermap[wl] = []
            lowermap[wl].append(word)

        for word in wordlist:
            wv = devowel(word)
            if not wv in vowelmap:
                vowelmap[wv] = []
            vowelmap[wv].append(word)

        # this is tracking all the words for a given key, but we only need to track the first occurrence for the same match
        # print("lowermap", lowermap)
        # print("vowelmap", vowelmap)

        results = []
        for word in queries:
            if word in s:
                results.append(word)
            elif word.lower() in lowermap:
                results.append(lowermap[word.lower()][0])
            elif devowel(word) in vowelmap:
                results.append(vowelmap[devowel(word)][0])
            else:
                results.append("")

        return results

s = Solution()
assert s.spellchecker(["KiTe","kite","hare","Hare"],
    ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]) == \
        ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
