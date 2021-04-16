from colorama import init, Fore

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # what kind of solution would this be called? it's not using a stack or a 2 pointer approach, according to solutions on leetcode
        # the main slowness here is from constantly changing the string, which ends up creating a new string
        # It's still O(n*k) type of solution, just could be a bit more efficient

        # possibly this is a brute force solution. If we kept track of counts, we could save some effort
        # see Approach 1 vs Approach 2 in https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3710/discuss/929906/Javascript-5-solutions-(Two-Pointers-Stack-Brute-Force)-Implementation
        i = 0
        while i < len(s) - k + 1:
            # print(f"i:{i:2}, k:{k:2}, len(s): {len(s):2}", f"{s[:i]}{Fore.GREEN}{s[i]}{Fore.RESET}{s[i+1:]}")
            matching = True
            j = 0
            while j < k - 1:
                # print(f"comparing {s[i + j]} to {s[i + j + 1]}")
                if s[i + j] != s[i + j + 1]:
                    matching = False
                    break
                j += 1

            if matching:
                # print(f"removing {s[:i]}{Fore.RED}{s[i:i+k]}{Fore.RESET}{s[i+k:]}")
                s = s[:i] + s[i+k:]
                i = max(0, i - k) # advance i backward by at most k characters
            else:
                i += max(1, j) # advance i forward by at least 1 but up to j characters

        # print(f"final result: '{s}'")
        return s

s = Solution()
assert s.removeDuplicates("abcd", 2) == "abcd"
assert s.removeDuplicates("abcdefghi", 20) == "abcdefghi"
assert s.removeDuplicates("aaabbbcccddd", 3) == ""
assert s.removeDuplicates("ffeeddccaabbbacdef", 3) == ""
assert s.removeDuplicates("deeedbbcccbdaa", 3) == "aa"
assert s.removeDuplicates("pbbcggttciiippooaais", 2) == "ps"

import importlib
inputs = importlib.import_module("remove-all-adjacent-duplicates-in-string-ii-input")
s.removeDuplicates(inputs.longStr, inputs.k)