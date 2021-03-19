from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # BFS approach
        # There's also an iterative DFS that looks pretty similar https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/discuss/133855/Straight-Forward
        # There's a recursive DFS too, which I don't recall how to approach https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/discuss/1116703/Python-Simple-dfs-+-oneliner-explained
        # I should probably brush up on adjacency matrices at some point, too

        keys = set([0])
        visit = [k for k in rooms[0]]
        while visit:
            k = visit.pop(0)

            keys.add(k)
            for l in rooms[k]:
                if l not in keys:
                    visit.append(l)

            # if k not in keys:
            #     keys.add(k)
            #     visit.extend(l for l in rooms[k])

        return len(keys) == len(rooms)


s = Solution()
assert s.canVisitAllRooms([[]]) == True
assert s.canVisitAllRooms([[], []]) == False

assert s.canVisitAllRooms([[1], []]) == True
assert s.canVisitAllRooms([[1], [0]]) == True
assert s.canVisitAllRooms([[1], [1]]) == True

assert s.canVisitAllRooms([[0], [1], [2], [3]]) == False

# test cases from problem description
assert s.canVisitAllRooms([[1], [2], [3], []]) == True
assert s.canVisitAllRooms([[1,3], [3,0,1], [2], [0]]) == False
