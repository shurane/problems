from typing import Optional
from helpers2 import TreeNode

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        result = self.findRecursive(root, root, k)
        return result != None

    def findNode(self, tree: TreeNode, val: int) -> Optional[TreeNode]:
        # takes log n to search the tree for 'val'
        # returns node if found, otherwise returns None
        if val == tree.val:
            return tree
        elif tree.left != None and val < tree.val:
            return self.findNode(tree.left, val)
        elif tree.right != None and val > tree.val:
            return self.findNode(tree.right, val)
        else:
            return None
        pass

    def findRecursive(self, node: TreeNode, tree: TreeNode, target: int) -> Optional[TreeNode]:
        remainder = target - node.val
        other = self.findNode(tree, remainder)
        if other != None and remainder != node.val: #disqualify node.val being half of target
            return other
        else:
            if node.left != None:
                leftside = self.findRecursive(node.left, tree, target)
                if leftside != None:
                    return leftside

            if node.right != None:
                rightside = self.findRecursive(node.right, tree, target)
                if rightside != None:
                    return rightside

            return None

# O(nlogn) without using any extra space in 41 minutes
# it's interesting, there are quite a few solutions to this.
# see this discussion: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/