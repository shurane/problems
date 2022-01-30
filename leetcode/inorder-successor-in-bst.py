from typing import Optional, List
from helpers2 import TreeNode, create_tree, inorder

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode, ancestors: List[TreeNode] = []) -> Optional[TreeNode]:
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p, [root] + ancestors)
        elif root.val < p.val:
            return self.inorderSuccessor(root.right, p, [root] + ancestors)
        else: # root == p
            successor = root.right
            while successor and successor.left:
                successor = successor.left

            if not successor:
                # first ancestor with val > p.val is a successor
                # print("root == p", p.val, ancestors)
                for ancestor in ancestors:
                    if ancestor.val > p.val:
                        successor = ancestor
                        break
            return successor

    def inorderSuccessorStack(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Doesn't save time. The tree is not that big anyway.
        # the difference between stack and ancestors is just a few allocations worth
        stack = []

        def helper(node: TreeNode) -> Optional[TreeNode]:
            if p.val < node.val:
                stack.append(node)
                value = helper(node.left)
                stack.pop()
                return value
            elif node.val < p.val:
                stack.append(node)
                value = helper(node.right)
                stack.pop()
                return value
            else: # node == p
                successor = node.right
                while successor and successor.left:
                    successor = successor.left

                if not successor:
                    # first ancestor with val > p.val is a successor
                    # print("node == p", p.val, chain)
                    for ancestor in reversed(stack):
                        if ancestor.val > p.val:
                            successor = ancestor
                            break
                return successor

        return helper(root)

s = Solution()

t1 = create_tree([2,1,3])
assert s.inorderSuccessor(t1, t1.left) == t1
assert s.inorderSuccessor(t1, t1) == t1.right
assert s.inorderSuccessor(t1, t1.right) == None

t2 = create_tree([8,4,12,2,6,10,14,1,3,5,7,9,11,13,15])
t2_inorder = list(inorder(t2))

for i in range(len(t2_inorder) - 1):
    # print(t2_inorder[i], s.inorderSuccessor(t2,t2_inorder[i]))
    assert s.inorderSuccessor(t2, t2_inorder[i]) == t2_inorder[i+1]
    assert s.inorderSuccessorStack(t2, t2_inorder[i]) == t2_inorder[i+1]

assert s.inorderSuccessor(t2, t2_inorder[-1]) == None
assert s.inorderSuccessorStack(t2, t2_inorder[-1]) == None