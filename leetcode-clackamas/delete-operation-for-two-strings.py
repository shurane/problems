from typing import Dict, Tuple, List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103214/Java-DP-Solution-(Longest-Common-Subsequence)
        # essentially Longest Common Subsequence -- so not quite edit distance... like with minDistance2
        d = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    d[i][j] = 0
                else:
                    if word1[i-1] == word2[j-1]:
                        d[i][j] = d[i-1][j-1] + 1
                    else:
                        d[i][j] = max(d[i-1][j], d[i][j-1])

        # print(*(" ".join([f"{i:2}" for i in row]) for row in d), sep="\n")
        lcs = d[len(word1)][len(word2)]
        # remove lcs from word1 and word2 and get the result
        return len(word1) - lcs + len(word2) - lcs

    def minDistance2(self, word1: str, word2: str) -> int:
        # https://leetcode.com/problems/delete-operation-for-two-strings/discuss/1196751/Python3-DFS-%2B-Memoization
        # basically top down DP
        d = dict()
        result = self.helper2(word1, word2, 0, 0, d)
        # print(d)
        return result

    def helper2(self, word1: str, word2: str, i, j, d: Dict[Tuple[int, int], int]) -> int:
        if (i, j) in d: return d[(i, j)]

        value = None

        # if word1 or word2 is used up, count up what's left in the other word
        if i == len(word1):
            value = len(word2) - j
        elif j == len(word2):
            value = len(word1) - i
        # skip the letter, since it's the same on both
        elif word1[i] == word2[j]:
            value = self.helper2(word1, word2, i + 1, j + 1, d)
        else:
            value = 1 + min(self.helper2(word1, word2, i + 1, j,     d),
                            self.helper2(word1, word2, i,     j + 1, d))

        d[(i, j)] = value
        return value

    def minDistance3(self, word1: str, word2: str) -> int:
        # bottom up DP https://leetcode.com/problems/delete-operation-for-two-strings/discuss/465701/Python-Bottom-up-DP-Approach
        d = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    d[0][0] = 0
                elif i == 0:
                    d[i][j] = d[i][j-1] + 1
                elif j == 0:
                    d[i][j] = d[i-1][j] + 1
                elif word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1]) + 1

        # print(*(" ".join([f"{i:2}" for i in row]) for row in d), sep="\n")

        return d[len(word1)][len(word2)]

    def minDistance4(self, word1: str, word2: str) -> int:
        d = dict()
        result = self.helper4(word1, word2, d)
        # print(d)
        return result

    def helper4(self, word1: str, word2: str, d: Dict[Tuple[str, str], int]) -> int:

        if word1 == word2:
            return 0

        shortest = maxsize
        # this is correct but takes up a lot of space... how to reduce?
        if (word1, word2) in d:
            shortest = min(shortest, d[(word1, word2)])
        if shortest != maxsize: return shortest

        for i in range(len(word1)):
            temp = word1[:i] + word1[i+1:]
            shortest = min(shortest, self.helper4(temp, word2, d))

        for i in range(len(word2)):
            temp = word2[:i] + word2[i+1:]
            shortest = min(shortest, self.helper4(word1, temp, d))

        d[(word1, word2)] = shortest + 1

        return shortest + 1

s = Solution()

assert s.minDistance("sea", "eat") == 2
assert s.minDistance("leetcode", "etco") == 4
assert s.minDistance("sea", "ate") == 4