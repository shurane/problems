class Solution:
    def convertToTitle(self, n: int) -> str:
        # I got my base 26 mixed up, and was very thrown off by starting at 1 instead of 0
        # https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation helped a lot

        m = dict(zip(range(0, 26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        letters = []
        # print("n", "q", "r", "m[r]", "title", sep="\t")
        while n > 0:
            q = (n - 1) // 26
            r = (n - 1) % 26
            letters.append(m[r])
            # print(n, q, r, m[r], "".join(reversed(letters)), sep="\t")
            n = q

        return "".join(reversed(letters))

s = Solution()

assert s.convertToTitle(1) == "A"
assert s.convertToTitle(26) == "Z"
assert s.convertToTitle(27) == "AA"
assert s.convertToTitle(28) == "AB"
assert s.convertToTitle(28) == "AB"
assert s.convertToTitle(702) == "ZZ" # 26 ** 2 + 26 ** 1
assert s.convertToTitle(703) == "AAA"
assert s.convertToTitle(18278) == "ZZZ" # 26 ** 3 + 26 ** 2 + 26 ** 1

# 35 min. Kind of embarassing, but I'm really rusty anyway.