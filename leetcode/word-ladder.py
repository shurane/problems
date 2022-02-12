from typing import List, Deque, Tuple
from collections import deque, defaultdict

class Solution:
    # https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        queue: Deque[Tuple[str, int]] = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghikjlmnopqrstuvwxyz":
                    nextword = word[:i] + c + word[i+1:]
                    if nextword in wordset:
                        wordset.remove(nextword)
                        queue.append((nextword, length + 1))

        return 0

s = Solution()
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert s.ladderLength("a", "c", ["a","b","c"]) == 2
assert s.ladderLength("hot", "dog", ["hot","dog"]) == 0

s.ladderLength("qa","sq",
              ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])