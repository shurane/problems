from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> Optional['Node']:
        if not node: return None

        copyNode = Node(node.val)
        graph = dict()
        graph[copyNode.val] = copyNode
        queue = [(node, copyNode)]
        while queue:
            nextQueue = []
            for original, copy in queue:
                for nei in original.neighbors:
                    if nei.val not in graph:
                        graph[nei.val] = Node(nei.val)
                        nextQueue.append((nei, graph[nei.val]))
                    copy.neighbors.append(graph[nei.val])
            queue = nextQueue
        return copyNode

    def cloneGraphTrackingEdges(self, node: 'Node') -> Optional['Node']:
        if not node: return None

        copyNode = Node(node.val)
        visited = set()
        graph = dict()
        graph[copyNode.val] = copyNode
        queue = [(node, copyNode)]
        while queue:
            nextQueue = []
            for original, copy in queue:
                for nei in original.neighbors:
                    lower, higher = sorted([original.val, nei.val])
                    if (lower, higher) in visited:
                        continue

                    visited.add((lower, higher))

                    if nei.val not in graph:
                        graph[nei.val] = Node(nei.val)

                    copy.neighbors.append(graph[nei.val])
                    graph[nei.val].neighbors.append(copy)
                    nextQueue.append((nei, graph[nei.val]))

            queue = nextQueue

        return copyNode
