class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, k:int = 2) -> int:
        if k == 0: return 0
        l = 0
        r = 0
        maxlen = 0
        unique = 0
        counts = [0] * 128
        while r < len(s):
            rcode = ord(s[r]) - 97
            counts[rcode] += 1
            if counts[rcode] == 1:
                unique += 1

            if unique > k:
                maxlen = max(maxlen, r - l)
                # print("found a unique substring with 2 characters", s[l:r])
                while unique > k:
                    lcode = ord(s[l]) - 97
                    counts[lcode] -= 1
                    if counts[lcode] == 0:
                        unique -= 1
                    l += 1
            r += 1

        return max(maxlen, r - l)

    def onepass(self, s: str) -> int:
        # found when checking the quickest submission times
        # this tracks changes between successive letters and stores the index
        # when it checks s[i] vs s[change] and s[change-1], s[start] gets updated if all 3 are different values
        start = 0
        change = 0
        maxlen = 1
        i = 0
        for i in range(1, len(s)):
            # print(f"start:{start} {s[start]}, change:{change} {s[change]}, i:{i} {s[i]}, {s[start:i]}")
            if s[i] != s[change]:
                if s[i] != s[change - 1]:
                    start = change
                change = i
            maxlen = max(maxlen, i - start + 1)
        # print(maxlen)
        return maxlen

    def onepassTrack(self, s:str) -> int:
        # also found when checking submission times
        maxlen = 0
        first = None
        second = None
        count = 0
        countsecond = 0
        for c in s:
            if c == first or c == second:
                count += 1
            else:
                count = countsecond + 1

            if c == second:
                countsecond += 1
            else:
                first, second = second, c
                countsecond = 1

            maxlen = max(maxlen, count)

        return maxlen


s = Solution()

assert s.lengthOfLongestSubstringTwoDistinct("eceba") == 3
assert s.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5
assert s.lengthOfLongestSubstringTwoDistinct("abbcccdddd") == 7
assert s.lengthOfLongestSubstringTwoDistinct("ddddcccbba") == 7
assert s.lengthOfLongestSubstringTwoDistinct("ababcc") == 4

assert s.onepass("a") == 1
assert s.onepass("eceba") == 3
assert s.onepass("ccaabbb") == 5
assert s.onepass("abbcccdddd") == 7
assert s.onepass("ddddcccbba") == 7
assert s.onepass("ababcc") == 4
assert s.onepass("baabcc") == 4

assert s.onepassTrack("eceba") == 3
assert s.onepassTrack("ccaabbb") == 5
assert s.onepassTrack("abbcccdddd") == 7
assert s.onepassTrack("ddddcccbba") == 7
assert s.onepassTrack("ababcc") == 4
assert s.onepassTrack("baabcc") == 4