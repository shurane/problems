from typing import NamedTuple, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

class ParentChild(NamedTuple):
    parent: TreeNode
    child: TreeNode
    level: int

# def fromList(lst):
    # if not lst:
        # return None
    # root = TreeNode()
    # for i, value in enumerate(lst):


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # print(f"isCousins(): root:{root}, x:{x}, y:{y})")
        if not root:
            return False

        q = [ParentChild(None, root, 0)]
        results = []

        # BFS approach
        while q:
            parent, node, level = q.pop(0)
            # print(f"q.pop(): parent:{parent}, node:{node}, level:{level}")

            maybeResult = self.helper(parent, node, x, y, level)
            if maybeResult:
                results.append(maybeResult)

            if node.left:
                q.append(ParentChild(node, node.left, level + 1))

            if node.right:
                q.append(ParentChild(node, node.right, level + 1))

        # print(results)
        return len(results) == 2 \
                and results[0].level == results[1].level \
            and results[0].parent.val != results[1].parent.val


    def helper(self, parent: TreeNode, node: TreeNode, x: int, y: int, level: 0) -> Optional[ParentChild]:
        if not parent or not node:
            return None

        if node.val == x or node.val == y:
            return ParentChild(parent, node, level)


s = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(5)

assert s.isCousins(t1, 4, 3) == False
assert s.isCousins(t2, 5, 4) == True
assert s.isCousins(None, 5, 4) == False
