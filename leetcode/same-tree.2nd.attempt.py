from helpers2 import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            #p.val == q.val, check their children
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        