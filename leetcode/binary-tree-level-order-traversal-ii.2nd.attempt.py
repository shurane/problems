from helpers2 import TreeNode
from typing import List

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # this should be faster... but it doesn't seem to be much faster
        queue = deque()
        queue.append((root, 0))
        results = []

        while queue:
            node, level = queue.popleft()

            if len(results) <= level:
                results.append([])

            results[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return list(reversed(results))

    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, 0)]
        results = []

        while queue:

            # slow since it needs to shift array over for every pop()
            node, level = queue.pop(0)

            if len(results) <= level:
                results.append([])

            results[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return list(reversed(results))