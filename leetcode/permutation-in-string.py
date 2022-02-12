class Solution:
    # TODO with only one dict(): https://leetcode.com/problems/permutation-in-string/discuss/638531/Java-or-C%2B%2B-or-Python3-or-Detailed-explanation-or-O(N)-time
    def checkInclusion(self, s: str, t: str) -> bool:
        sdict = dict()
        for letter in s:
            if letter not in sdict:
                sdict[letter] = 0
            sdict[letter] += 1

        tdict = dict()
        k = len(s)
        count = 0

        # print(s, "len", len(s), sdict)
        for i in range(len(t)):
            letter = t[i]
            if letter not in tdict:
                tdict[letter] = 0
            tdict[letter] += 1

            if letter in sdict and tdict[letter] <= sdict[letter]:
                count += 1

            if i-k >= 0:
                prev = t[i-k]
                if prev in sdict and tdict[prev] <= sdict[prev]:
                    count -= 1
                tdict[prev] -= 1

            # print(i, "count:", count, letter, {k:v for k,v in tdict.items() if v != 0})

            if count == len(s):
                return True

        return False

s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("abc", "cba") == True
assert s.checkInclusion("abcd", "cba") == False
assert s.checkInclusion("aaab", "aaaaaab") == True
assert s.checkInclusion("aaab", "aaaaaaaab") == True
assert s.checkInclusion("aaaaabb", "aaaaaab") == False
assert s.checkInclusion("aaaaabb", "baaaaaab") == False
assert s.checkInclusion("aaaaabb", "aaaaaabb") == True
assert s.checkInclusion("qff", "ifisnoskikfqzrmzlv") == False

assert s.checkInclusion("abc", "aabbccaaccbb") == False
assert s.checkInclusion("aa", "ababababa") == False