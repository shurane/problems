from typing import List, Dict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        key = dict(zip(order, range(26)))

        for i in range(len(words) - 1):
            if compare(words[i], words[i+1], key) > 0:
                return False
        return True

def compare(left, right, key: Dict[str, int]) -> int:
    # print(left, right)
    for l, r in zip(left, right):
        # print(f"> left:{l}, right:{r}")
        if key[l] < key[r]:
            return -1
        elif key[l] > key[r]:
            return 1

    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    return 0



s = Solution()
assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") ==  True
assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
assert s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
assert s.isAlienSorted(["apple"], "abcdefghijklmnopqrstuvwxyz") == True