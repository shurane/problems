class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        # 2 passes. O(n)
        # 1st pass involves counting up each letter
        # 2nd pass returns the first letter whose count is 1
        # otherwise return -1

        # is there a way to do faster than 2 passes?
        # I can't tell if there is. Can iterate over 's' and count each char in 's', but I think that's O(n*2)
        # but my solution runtime is much slower than others

        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        for i in range(len(s)):
            letter = s[i]
            if counts[letter] == 1:
                return i
        
        return -1

    def firstUniqChar2(self, s: 'str') -> 'int':
        # inspiration from https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!

        # this is faster than O(n*2), since for even a long string, it only has to count once for each letter.
        # For 26 letters, scanning 's' for the count takes O(n). Then finding the first occurrence takes O(n).
        # Total of 26 * 2 * O(n), which is still just O(n). 
        # Apparently it's faster than the hashmap variant since it relies on fast, built-in C code
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indices = []
        for letter in letters:
            if s.count(letter) == 1:
                indices.append(s.index(letter))
        
        if len(indices) == 0:
            return -1
        return min(indices)

    def firstUniqChar3(self, s: 'str') -> 'int':
        # inspiration from https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86511/Java-One-Pass-Solution-with-LinkedHashMap
        # could use ordereddict here, same idea as LinkedHashSet. Maintains order of insertions
        from collections import OrderedDict
        counts = OrderedDict()
        seen = set() # could easily be a 26 index array for count at each character
        for i in range(len(s)):
            letter = s[i]
            if letter not in seen:
                counts[letter] = i
                seen.add(letter)
            else:
                if letter in counts:
                    del counts[letter]

        if len(counts) == 0:
            return -1
        return next(iter(counts.items()))[1]

s = Solution()

assert s.firstUniqChar3("leetcode") == 0
assert s.firstUniqChar3("loveleetcode") == 2
assert s.firstUniqChar3("aaaa") == -1

# 5 minutes for orgional solution. Another 10-15 minutes for solutions 2 and 3