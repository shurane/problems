from typing import List
from helpers import TreeNode

class Solution:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root