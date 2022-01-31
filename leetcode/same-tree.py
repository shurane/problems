from helpers2 import TreeNode, create_tree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)

a = create_tree([1])
b = create_tree([1,5])
c = create_tree([1,None,7,None,None,3])
d = create_tree([1])
e = create_tree([1,5])

f = TreeNode(1)
f.right = TreeNode(7)
f.right.left = TreeNode(3)

s = Solution()
assert s.isSameTree(a,d) == True
assert s.isSameTree(b,e) == True
assert s.isSameTree(c,f) == True
assert s.isSameTree(a,f) == False
