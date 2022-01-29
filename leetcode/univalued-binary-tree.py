# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isVal(root, root.val)

    def isVal(self, tree: TreeNode, value) -> bool:
        if not tree:
            return True
        elif tree.val != value:
            return False
        else:
            return self.isVal(tree.left, value) and self.isVal(tree.right, value)

# 2 minutes