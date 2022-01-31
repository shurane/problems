from helpers2 import TreeNode

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