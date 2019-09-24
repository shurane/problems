class Solution:
    def isAnagramDoubleMemory(self, s: str, t: str) -> bool:
        countForS = [0 for i in range(26)]
        countForT = [0 for i in range(26)]

        for c in s:
            countForS[ord(c) - ord("a")] += 1
        for c in t:
            countForT[ord(c) - ord("a")] += 1

        return countForS == countForT

    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0 for i in range(26)]

        for c in s:
            counts[ord(c) - ord("a")] += 1
        for c in t:
            counts[ord(c) - ord("a")] -= 1

        return all(n == 0 for n in counts)

s = Solution()
assert s.isAnagram("", "") == True
assert s.isAnagram("abc", "abc") == True
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("anagram", "nagara") == False
assert s.isAnagram("rat", "car") == False
assert s.isAnagram("a", "aa") == False
assert s.isAnagram("", "a") == False
assert s.isAnagram("a", "") == False