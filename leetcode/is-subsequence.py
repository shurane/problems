class Solution:
    def isSubsequenceIterative(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return s in t
        i = 0
        for c in s:
            found = False
            while i < len(t):
                # print(c, i, found)
                if t[i] == c:
                    found = True
                    i += 1
                    break
                else:
                    i += 1
            if not found:
                return False

        return True

    def isSubsequenceRecursive(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for i, c in enumerate(s):
            foundC = t.find(c)
            if foundC == -1:
                return False
            return self.isSubsequenceRecursive(s[i+1:], t[foundC+1:])

    def isSubsequenceDPExpanded(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        m = [-1 for c in s]
        m[0] = t.find(s[0])
        i = 1
        while i < len(s):
            if m[i - 1] != -1:
                m[i] = t.find(s[i], m[i - 1] + 1)

            i += 1

        return m[-1] != -1

    def isSubsequenceDPShortened(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        charSeen = t.find(s[0])
        i = 1
        while i < len(s):
            if charSeen != -1:
                charSeen = t.find(s[i], charSeen + 1)

            i += 1

        return charSeen != -1

s = Solution()

assert s.isSubsequenceDPShortened("", "ahbgdc") == True
assert s.isSubsequenceDPShortened("a", "a") == True
assert s.isSubsequenceDPShortened("a", "b") == False
assert s.isSubsequenceDPShortened("ba", "ab") == False
assert s.isSubsequenceDPShortened("abc", "ahbgdc") == True
assert s.isSubsequenceDPShortened("axc", "ahbgdc") == False
assert s.isSubsequenceDPShortened("a" * 10, "a" * 10) == True
assert s.isSubsequenceDPShortened("a" * 10, "a" * 9) == False
assert s.isSubsequenceDPShortened("a" * 9, "a" * 10) == True