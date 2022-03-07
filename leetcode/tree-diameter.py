from typing import List

class Solution:
    # This is a list of edges. It just happens to be a tree in structure.
    # We're trying to find the two farthest nodes from each other as well.
    # Seems like this can be set up as BFS/DFS.
    # Maybe it can also be set as union find?

    # Intuition is in the hints.
    # 1. Find the farthest node B from any node A
    # 2. Find the farthest node C from node B
    # Tree Diameter is between B and C
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges: return 0
        graph = dict()

        for a,b in edges:
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        def helper(node):
            distances = dict()
            farthest = -1
            farthestDistance = 0
            queue = [(node, 0)]
            while queue:
                nextQueue = []
                for elem, distance in queue:
                    if distance > farthestDistance:
                        farthest = elem
                        farthestDistance = distance
                    for neighbor in graph[elem]:
                        if (elem, neighbor) not in distances:
                            distances[(elem, neighbor)] = distance + 1
                            distances[(neighbor, elem)] = distance + 1
                            nextQueue.append((neighbor, distance+1))
                queue = nextQueue

            # print(f"farthest is {node}>{farthest} distance: {distance}")
            return farthest, farthestDistance

        a, _ = helper(0)
        b, bdist = helper(a)

        return bdist

    # looked at some solutions, don't need to track distance at every step
    # think of it as level order traversal and increment distance at each level
    def treeDiameterShorter(self, edges: List[List[int]]) -> int:
        if not edges: return 0
        graph = dict()

        for a,b in edges:
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        def helper(node):
            farthest = -1
            distance = -1
            queue = [(node, -1)]
            while queue:
                nextQueue = []
                for farthest, parent in queue:
                    for neighbor in graph[farthest]:
                        if neighbor != parent:
                            nextQueue.append((neighbor, farthest))
                queue = nextQueue
                distance += 1

            # print(f"farthest is {node}>{farthest} distance: {distance}")
            return farthest, distance

        a, _ = helper(0)
        b, bdist = helper(a)

        return bdist

    def treeDiameterLeaves(self, edges: List[List[int]]) -> int:
        if not edges: return 0
        graph = dict()

        for a,b in edges:
            if a not in graph: graph[a] = set()
            if b not in graph: graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)

        # grab all the leaves and process them
        queue = []
        for elem in graph:
            if len(graph[elem]) == 1: queue.append(elem)

        levelsProcessed = 0
        edgesLeft = len(edges) + 1
        while edgesLeft > 2:
            # print(f"leaves, {queue}, edgesLeft: {edgesLeft}")
            edgesLeft -= len(queue)
            nextQueue = []
            for elem in queue:
                # print(f"processing {elem}, {graph[elem]}")
                if graph[elem]:
                    neighbor = graph[elem].pop()
                    graph[neighbor].remove(elem)
                    if len(graph[neighbor]) == 1:
                        nextQueue.append(neighbor)

            levelsProcessed += 1
            queue = nextQueue

        # print(f"levels processed: {levelsProcessed}, edgesLeft: {edgesLeft}")
        if edgesLeft == 1:
            return levelsProcessed * 2
        else:
            return levelsProcessed * 2 + 1

s = Solution()
assert s.treeDiameter([]) == 0
assert s.treeDiameter([[0,1],[0,2]]) == 2
assert s.treeDiameterShorter([[0,1],[0,2]]) == 2
assert s.treeDiameterLeaves([[0,1],[0,2]]) == 2
assert s.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]) == 4
assert s.treeDiameterShorter([[0,1],[1,2],[2,3],[1,4],[4,5]]) == 4
assert s.treeDiameterLeaves([[0,1],[1,2],[2,3],[1,4],[4,5]]) == 4