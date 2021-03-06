from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encoding = ""
        # sort words from longest to shortest
        for word in sorted(words, key=len, reverse=True):
            # check if word is a substring of encoding so far
            if f"{word}#" in encoding:
                continue
            encoding += f"{word}#"

        # this is not the most efficient, since we're doing a substring check for each word in wording.
        # num of words = M, len of encoding = N
        # runtime is O(M * N)

        return len(encoding)

# time, me, timer, timers -> timers#
