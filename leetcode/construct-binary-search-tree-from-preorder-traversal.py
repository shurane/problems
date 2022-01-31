from typing import Optional, List
from helpers2 import TreeNode, create_tree, inorder, preorder as ppreorder

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(start: int, end: int) -> Optional[TreeNode]:
            if start > end or end > n - 1:
                return None

            root = TreeNode(preorder[start])

            i = start + 1
            while i <= end and preorder[i] < preorder[start]:
                i += 1

            root.left = helper(start + 1, i - 1)
            root.right = helper(i, end)

            return root

        n = len(preorder)
        result = helper(0, n - 1)
        # print([t.val for t in list(ppreorder(result))])
        return result

s = Solution()

input1 = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
t1 = create_tree(input1)
input1preorder = [t.val for t in list(ppreorder(t1))]
assert [t.val for t in ppreorder(s.bstFromPreorder(input1preorder))] == input1preorder

t2 = TreeNode(0)
c = t2
for i in range(1,11):
    c.right = TreeNode(i)
    c = c.right

t3 = TreeNode(10)
c = t3
for i in range(9,-1,-1):
    c.left = TreeNode(i)
    c = c.left

t2preorder = [t.val for t in ppreorder(t2)]
t3preorder = [t.val for t in ppreorder(t3)]
assert [t.val for t in ppreorder(s.bstFromPreorder(t2preorder))] == t2preorder
assert [t.val for t in ppreorder(s.bstFromPreorder(t3preorder))] == t3preorder