import time
import blessings
term = blessings.Terminal()

def colorizedStr(s, reds=[], blues=[], yellows=[]):
    newS = ""
    for j in range(len(s)):
        if j in reds:
            newS += term.red(s[j])
        elif j in blues:
            newS += term.blue(s[j])
        elif j in yellows:
            newS += term.yellow(s[j])
        else:
            newS += s[j]
    return newS

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # very similar to smallest substring of all characters
        seen = {}

        maxString = ""
        uniqueBegin = 0

        for i, letter in enumerate(s):
            print "             {}"\
                    .format(colorizedStr(s, reds=[i], yellows=range(uniqueBegin,i)))

            # we are going to make sure the count of each letter is at most 1
            if letter in seen:
                print "dupe of '{}': {}"\
                        .format(letter, colorizedStr(s, blues=[seen[letter], i]))
                # skip to one past the last seen occurrence of letter
                uniqueBegin = seen[letter] + 1

            seen[letter] = i

            sub = s[uniqueBegin:i+1]

            if len(sub) > len(maxString):
                maxString = sub

        return maxString



s = Solution()

assert s.lengthOfLongestSubstring("abcabcbb") == "abc"
assert s.lengthOfLongestSubstring("bbbbb") == "b"
assert s.lengthOfLongestSubstring("pwwkew") == "wke"

