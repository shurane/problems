from typing import List
from helpers2 import compareListOfLists

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            key = tuple(score(s))
            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        # print(groups)
        return groups.values()

    def groupAnagramsWithSort(self, strs: List[str]) -> List[List[str]]:
        matches = dict()
        for word in strs:
            sword = "".join(sorted(word))
            if sword not in matches:
                matches[sword] = []
            matches[sword].append(word)

        return list(matches.values())

def score(s: str):
    counts = [0 for i in range(26)]
    for c in s:
        counts[ord(c) - ord("a")] += 1

    return counts

s = Solution()
assert compareListOfLists(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]) == True

assert compareListOfLists(s.groupAnagrams([]), []) == True
assert compareListOfLists(s.groupAnagrams(["eat", "tea"]), [["eat", "tea"]]) == True
assert compareListOfLists(s.groupAnagrams(["eat", "tear"]), [["eat"], ["tear"]]) == True

assert compareListOfLists(s.groupAnagramsWithSort(["eat", "tea", "tan", "ate", "nat", "bat"]), [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]) == True

assert compareListOfLists(s.groupAnagramsWithSort([]), []) == True
assert compareListOfLists(s.groupAnagramsWithSort(["eat", "tea"]), [["eat", "tea"]]) == True
assert compareListOfLists(s.groupAnagramsWithSort(["eat", "tear"]), [["eat"], ["tear"]]) == True