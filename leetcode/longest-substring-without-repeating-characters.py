# import blessings
# term = blessings.Terminal()

# def colorizedStr(s, reds=[], blues=[], yellows=[]):
    # newS = ""
    # for j in range(len(s)):
        # if j in reds:
            # newS += term.red(s[j])
        # elif j in blues:
            # newS += term.blue(s[j])
        # elif j in yellows:
            # newS += term.yellow(s[j])
        # else:
            # newS += s[j]
    # return newS

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # very similar to smallest substring of all characters
        seen = {}

        maxString = ""
        begin = 0

        for i, letter in enumerate(s):
            # print "        {}, {}, {}"\
                    # .format(colorizedStr(s, reds=[i], yellows=range(begin,i)), maxString, seen)

            # we are going to make sure the count of each letter is at most 1
            if letter in seen:
                if begin <= seen[letter]:
                    # print "dupe {}: {}"\
                            # .format(letter, colorizedStr(s, blues=[seen[letter], i]))
                    # skip to one past the last seen occurrence of letter
                    begin = seen[letter] + 1

            seen[letter] = i

            sub = s[begin:i+1]

            if len(sub) > len(maxString):
                maxString = sub

        return len(maxString)

# s = Solution()
# assert s.lengthOfLongestSubstring("abcabcbb") == 3
# assert s.lengthOfLongestSubstring("bbbbb") == 1
# assert s.lengthOfLongestSubstring("pwwkew") == 3
# assert s.lengthOfLongestSubstring("abba") == 2

