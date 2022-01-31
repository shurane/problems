from helpers2 import TreeNode, create_tree
import sys

class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif self.isLeaf(root):
            return 1
        else:
            left = None
            right = None
            if root.left:
                left = self.minDepth(root.left)

            if root.right:
                right = self.minDepth(root.right)

            if left and right:
                return 1 + min(left, right)
            elif left:
                return 1 + left
            else:
                return 1 + right

    def minDepthIterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif self.isLeaf(root):
            return 1

        nodes = [(1, root)]
        minDepth = sys.maxsize

        while nodes:
            depth, node = nodes.pop(0)
            # print(depth, node)
            if self.isLeaf(node) and depth < minDepth:
                minDepth = depth

            if node.left:
                nodes.append((depth + 1, node.left))
            if node.right:
                nodes.append((depth + 1, node.right))

        return minDepth

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right

t = create_tree([3, 9, 20, None, None, 15, 7])
t1 = create_tree([1, 2])
t2 = create_tree([1,2,3,4,5])
t3 = create_tree([])
t4 = create_tree([1])
t5 = create_tree(range(14))
t6 = create_tree(range(125))
t7 = create_tree(range(126))
s = Solution()
assert s.minDepthIterative(t) == 2
assert s.minDepthIterative(t1) == 2
assert s.minDepthIterative(t2) == 2
assert s.minDepthIterative(t3) == 0
assert s.minDepthIterative(t4) == 1
assert s.minDepthIterative(t5) == 4
assert s.minDepthIterative(t6) == 6
assert s.minDepthIterative(t7) == 7