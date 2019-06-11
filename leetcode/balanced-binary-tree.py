from helpers2 import TreeNode, create_tree

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif self.isNoneOrLeaf(root.left) and self.isNoneOrLeaf(root.right):
            return True
        else:
            diffLessThan1 = abs(self.height(root.left) - self.height(root.right)) <= 1
            if diffLessThan1:
                left  = self.isBalanced(root.left)
                right = self.isBalanced(root.right)
            
                # print("recursing", root.val, root.left and root.left.val, root.right and root.right.val, left, right)
                # return self.isBalanced(root.left) and self.isBalanced(root.right)
                return left and right
            else:
                return False
    
    def isNoneOrLeaf(self, node: TreeNode) -> bool:
        if not node:
            return True
        else:
            return not node.left and not node.right
    
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

import ast

t1 = None
with open("balanced-binary-tree-long.txt") as f:
    text = f.read().strip().replace("null", "None")
    lst = ast.literal_eval(text)
    t1 = create_tree(lst)

s = Solution()

print(s.height(t1))
print(s.isNoneOrLeaf(t1))
print(s.isBalanced(t1))