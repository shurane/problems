"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from typing import List

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        i = 1
        while True:
            nodes = self.helperDFS(root, 0, i)
            if not nodes:
                break
            if len(nodes) > 1:
                for a, b in zip(nodes[:-1], nodes[1:]):
                    a.next = b
            # don't need to do anything if len(nodes) == 1
            i += 1

        return root

    def helperDFS(self, node: 'Node', currentDepth: int, requiredDepth: int) -> List['Node']:
        # print(f"val={node and node.val}, currentDepth={currentDepth}, requiredDepth={requiredDepth}")
        if not node:
            return []
        elif currentDepth < requiredDepth:
            left = self.helperDFS(node.left, currentDepth + 1, requiredDepth)
            right = self.helperDFS(node.right, currentDepth + 1, requiredDepth)
            return left + right
        else:
            # currentDepth == requiredDepth
            # don't recurse, just return the current node
            return [node]

    def helperDFS2(self, node: 'Node', currentDepth: int, requiredDepth: int) -> List['Node']:
        # print(f"val={node and node.val}, currentDepth={currentDepth}, requiredDepth={requiredDepth}")
        if not node:
            return []
        elif currentDepth < requiredDepth:
            left = self.helperDFS(node.left, currentDepth + 1, requiredDepth)
            right = self.helperDFS(node.right, currentDepth + 1, requiredDepth)
            return left + right
        else:
            # currentDepth == requiredDepth
            # don't recurse, just return the current node
            return [node]