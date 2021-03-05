from collections import OrderedDict
from typing import List, Tuple, Dict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q: List[Tuple[int, int]] = [(root, 0)]
        averages: Dict[int, List[int]] = OrderedDict()

        while q:
            node, level = q.pop(0)
            if node:
                if not level in averages:
                    averages[level] = []
                averages[level].append(node.val)
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

        results = []
        for level, values in averages.items():
            results.append(sum(values) / len(values))

        return results

class Solution2:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = [root]
        values = []

        while q:
            levelsum = []
            levelnext = []
            while q:
                node = q.pop(0)
                if node:
                    levelnext.append(node.left)
                    levelnext.append(node.right)
                    levelsum.append(node.val)

            if levelsum:
                values.append(sum(levelsum) / len(levelsum))
            q = levelnext

        return values
