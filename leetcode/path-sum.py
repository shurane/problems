from helpers2 import TreeNode, create_tree

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif self.isLeaf(root) and root.val == sum:
            return True
        else:
            left = self.hasPathSum(root.left, sum - root.val)
            right = self.hasPathSum(root.right, sum - root.val)
            return left or right
    
    def isLeaf(self, node: TreeNode) -> bool:
        return node != None and node.left == None and node.right == None

s = Solution()

t0 = create_tree([5,4])
t1 = create_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
assert s.hasPathSum(t0, 9) == True
assert s.hasPathSum(t0, 5) == False
assert s.hasPathSum(t1, 22) == True
assert s.hasPathSum(t1, 23) == False
assert s.hasPathSum(t1, 1) == False