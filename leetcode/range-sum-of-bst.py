from helpers2 import TreeNode, create_tree

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif L <= root.val <= R:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        elif root.val <= L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R)

s = Solution()

t1 = create_tree([10,5,15,3,7,None,18])
t2 = create_tree([10,5,15,3,7,13,18,1,None,6])

# print(t1.printLevels())

assert s.rangeSumBST(t1, 7, 15) == 32
assert s.rangeSumBST(t2, 6, 10) == 23