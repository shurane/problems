from typing import List, Deque, Tuple
from collections import deque, defaultdict

class Solution:
    # https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
    # https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue: Deque[Tuple[str, int]] = deque([(beginWord, 1)])
        wordlookup = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                intermediateWord = word[:i] + "_" + word[i+1:]
                wordlookup[intermediateWord].append(word)

        visited = set([beginWord])
        # could do a level order BFS iteration here instead to skip using a queue
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                nextword = word[:i] + "_" + word[i+1:]
                for candidate in wordlookup[nextword]:
                    if candidate not in visited:
                        if candidate == endWord:
                            return length + 1
                        visited.add(candidate)
                        queue.append((candidate, length + 1))

        return 0

s = Solution()
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert s.ladderLength("a", "c", ["a","b","c"]) == 2
assert s.ladderLength("hot", "dog", ["hot","dog"]) == 0

s.ladderLength("qa","sq",
              ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])