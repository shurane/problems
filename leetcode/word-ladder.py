from typing import List, Deque, Dict, Optional
from collections import deque, defaultdict

class Solution:
    # https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95/609510
    # thanks @stuxen for a bidirectional BFS approach
    # But it needs to process all words in the queue with the same length,
    # otherwise we run into issues with words at the same distance.
    # Official solution takes this into account.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlookup: Dict[str, List[str]] = defaultdict(list)
        if endWord not in wordList: return 0

        for word in wordList:
            for i in range(len(word)):
                intermediateWord = word[:i] + "_" + word[i+1:]
                wordlookup[intermediateWord].append(word)

        # print("begin:", beginWord, "end:", endWord)
        # print("wordlookup")
        # for intermed, words in sorted(wordlookup.items()): print(intermed, words)
        def visit(queue: Deque[str], visited: Dict[str, int], others: Dict[str, int]):
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                length = visited[word]
                # print(word, length, "\nvisited", visited, "\n others", visited_others)
                for i in range(len(word)):
                    nextword = word[:i] + "_" + word[i+1:]
                    for candidate in wordlookup[nextword]:
                        if candidate in others:
                            return length + others[candidate]
                        if candidate not in visited:
                            if candidate == endWord:
                                return length + 1
                            visited[candidate] = length + 1
                            queue.append(candidate)
            return None

        vbegin: Dict[str, int] = {beginWord: 1}
        vend: Dict[str, int] = {endWord: 1}
        qbegin: Deque[str] = deque([beginWord])
        qend: Deque[str] = deque([endWord])
        ans: Optional[int] = None

        while qbegin and qend:
            # print("begin", list(qbegin), "\nvisit", vbegin, "\n  end", list(qend), "\nvisit", vend)
            ans = visit(qbegin, vbegin, vend)
            if ans: return ans
            ans = visit(qend, vend, vbegin)
            if ans: return ans

        return 0

    # https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
    # https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
    def ladderLengthSingleBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue: Deque[str] = deque([beginWord])
        wordlookup = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                intermediateWord = word[:i] + "_" + word[i+1:]
                wordlookup[intermediateWord].append(word)

        visited = {beginWord: 1}
        # could do a level order BFS iteration here instead to skip using a queue
        while queue:
            word = queue.popleft()
            length = visited[word]
            if word == endWord:
                return length

            for i in range(len(word)):
                nextword = word[:i] + "_" + word[i+1:]
                for candidate in wordlookup[nextword]:
                    if candidate not in visited:
                        visited[candidate] = length + 1
                        queue.append(candidate)

        return 0

s = Solution()
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert s.ladderLength("a", "c", ["a","b","c"]) == 2
assert s.ladderLength("hot", "dog", ["hot","dog"]) == 0
assert s.ladderLength("qa","sq", ["si","go","se","cm","so","ph","mt","db","mb",
    "sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra",
    "fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur",
    "rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb",
    "sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm",
    "an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io",
    "be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]) == 5

# hbo > hbw > qbw > qbx
assert s.ladderLength("hbo", "qbx", ["abo","hco","hbw","ado","abq","hcd","hcj","hww","qbq","qby","qbz","qbx","qbw"]) == 4
assert s.ladderLengthSingleBFS("hbo", "qbx", ["abo","hco","hbw","ado","abq","hcd","hcj","hww","qbq","qby","qbz","qbx","qbw"]) == 4