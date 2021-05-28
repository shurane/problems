from typing import List
from collections import defaultdict

class Solution:
    def maxProductAnswer(self, words: List[str]) -> int:
        # https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233802/Python-Bitmask-solution-explained
        # bitmask is definitely the way
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - ord('a'))

        for w1 in d.keys():
            for w2 in d.keys():
                if d[w1] & d[w2] == 0:
                    # if len(w1) * len(w2) > ans:
                    #     print(w1, w2)
                    ans = max(ans, len(w1)*len(w2))

        return ans

    def maxProduct(self, words: List[str]) -> int:
        # time limit exceeded for large inputs
        codes = dict()
        for word in words:
            wordcode = [False] * 26
            # mask = 0
            for l in word:
                val = ord(l) - ord('a')
                # mask |= 1 << val
                wordcode[val] = True
            codes[word] = tuple(wordcode)
            # codes[word] = mask

        best = 0
        for c in codes:
            for d in codes:
                count = 0
                left = 0
                right = 0
                for l, r in zip(codes[c], codes[d]):
                    if l ^ r: count += 1

                    if l: left += 1
                    if r: right += 1
                if count == left + right and len(c) * len(d) > best:
                    # print(count, left + right, len(c), len(d), len(c) * len(d), c, d)
                    best = max(best, len(c) * len(d))
        return best


s = Solution()
assert s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16
assert s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) == 4
assert s.maxProduct(["a","aa","aaa","aaaa"]) == 0
assert s.maxProduct(["a","ab","ac"]) == 0
assert s.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]) == 15
test = ["bdcecbcadca","caafd","bcadc","eaedfcd","fcdecf","dee","bfedd","ffafd","eceaffa","caabe","fbdb","acafbccaa","cdc","ecfdebaafde","cddbabf","adc","cccce","cbbe","beedf","fafbfdcb","ceecfabedbd","aadbedeaf","cffdcfde","fbbdfdccce","ccada","fb","fa","ec","dddafded","accdda","acaad","ba","dabe","cdfcaa","caadfedd","dcdcab","fadbabace","edfdb","dbaaffdfa","efdffceeeb","aefdf","fbadcfcc","dcaeddd","baeb","beddeed","fbfdffa","eecacbbd","fcde","fcdb","eac","aceffea","ebabfffdaab","eedbd","fdeed","aeb","fbb","ad","bcafdabfbdc","cfcdf","deadfed","acdadbdcdb","fcbdbeeb","cbeb","acbcafca","abbcbcbaef","aadcafddf","bd","edcebadec","cdcbabbdacc","adabaea","dcebf","ffacdaeaeeb","afedfcadbb","aecccdfbaff","dfcfda","febb","bfffcaa","dffdbcbeacf","cfa","eedeadfafd","fcaa","addbcad","eeaaa","af","fafc","bedbbbdfae","adfecadcabe","efffdaa","bafbcbcbe","fcafabcc","ec","dbddd","edfaeabecee","fcbedad","abcddfbc","afdafb","afe","cdad","abdffbc","dbdbebdbb"]
assert s.maxProductAnswer(test) == 45
assert s.maxProduct(test) == 45
