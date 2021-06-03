class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
        # damn, so impressive. I feel so out of touch after not doing dynamic programming problems for a few weeks.
        # And there's still a few other variations to the solution from OldCodingFarmer
        r, c, l = len(s1), len(s2), len(s3)

        if r + c != l: return False

        dp = [[True for i in range(c + 1)] for j in range(r + 1)]

        for i in range(1, r + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1+j] or \
                           dp[i][j-1] and s2[j-1] == s3[j-1+i]

        # return dp[-1][-1]
        return dp[r][c]

    # def isInterleaveFaulty(self, s1: str, s2: str, s3: str) -> bool:
    #     from colorama import init, Fore
    #     init()
    #     i = j = k = 0

    #     while k < len(s3):
    #         if i < len(s1) and s3[k] == s1[i]:
    #             # print(f"{s1[:i]}{Fore.BLUE}{s1[i]}{Fore.RESET}{s1[i+1:]} {s2} {s3[:k]}{Fore.BLUE}{s3[k]}{Fore.RESET}{s3[k+1:]}", i, j, k)
    #             k += 1
    #             i += 1
    #         elif j < len(s2) and s3[k] == s2[j]:
    #             # print(f"{s1} {s2[:j]}{Fore.GREEN}{s2[j]}{Fore.RESET}{s2[j+1:]} {s3[:k]}{Fore.GREEN}{s3[k]}{Fore.RESET}{s3[k+1:]}", i, j, k)
    #             k += 1
    #             j += 1
    #         else:
    #             return False

    #     print("reached the end", s3)
    #     return k == len(s3) and len(s1) + len(s2) == len(s3)

s = Solution()

assert s.isInterleave("", "", "") == True
assert s.isInterleave("a", "", "a") == True
assert s.isInterleave("", "b", "b") == True
assert s.isInterleave("a", "b", "ab") == True
assert s.isInterleave("a", "b", "ba") == True

assert s.isInterleave("a", "", "") == False
assert s.isInterleave("", "b", "") == False
assert s.isInterleave("a", "b", "") == False

assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False