from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # bottom up DP, see https://leetcode.com/problems/longest-string-chain/discuss/298884/Python-Using-dictionary
        dp = dict()
        for word in words:
            dp[word] = 1

        best = 1
        for word in sorted(words, key=len):
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
                best = max(best, dp[word])
        return best

s = Solution()
assert s.longestStrChain(["a", "bb", "ccc", "dddd"]) == 1
assert s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4
assert s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5
assert s.longestStrChain(["a","b","ab","bac"]) == 2