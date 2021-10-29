class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # https://backtobackswe.com/platform/content/minimum-window-substring/solutions
        # there's gotta be a more simpler to read solution than this...

        tcounts = dict()
        count = len(t)
        for letter in t:
            if letter not in tcounts:
                tcounts[letter] = 0
            tcounts[letter] += 1

        l = 0
        r = 0
        scounts = dict()
        min_window = s
        match_found = False
        while r < len(s):
            # print(f"r - {l}, {r}, count:{count}", s[l:r])

            letter = s[r]
            if letter not in scounts:
                scounts[letter] = 0
            scounts[letter] += 1

            if letter in tcounts and scounts[letter] <= tcounts[letter]:
                count -= 1

            while count == 0 and l <= r:
                # print("we have a match", s[l:r+1])
                # print(f"l - {l}, {r}, count:{count}", s[l:r+1])
                match_found = True
                if len(s[l:r]) < len(min_window):
                    min_window = s[l:r+1]

                if s[l] in tcounts and scounts[s[l]] <= tcounts[s[l]]:
                    count += 1
                scounts[s[l]] -= 1
                l += 1

            r += 1

        # print("min_window", min_window)
        if not match_found:
            return ""
        else:
            return min_window

s = Solution()
assert s.minWindow("a", "a") == "a"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("ABBBBBBBBBCemptyABC", "ABC") == "ABC"
assert s.minWindow("ABCemptyABBBBBBBBBC", "ABC") == "ABC"
assert s.minWindow("ABBBBBBBBBCemptyABCemptyABBBBBBBBBC", "ABC") == "ABC"
assert s.minWindow("CBBBABCBBBA", "ABC") == "ABC"
assert s.minWindow("ABBBCBABBBC", "ABC") == "CBA"
