from helpers import TreeNode, listToTree
import sys

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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

    def minDepthIterative(self, root):
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

    def isLeaf(self, node):
        return not node.left and not node.right

t = listToTree([3, 9, 20, None, None, 15, 7])
t1 = listToTree([1, 2])
t2 = listToTree([1,2,3,4,5])
t3 = listToTree([])
t4 = listToTree([1])
t5 = listToTree(range(14))
s = Solution()
print(s.minDepthIterative(t), "====\n")
print(s.minDepthIterative(t1), "====\n")
print(s.minDepthIterative(t2), "====\n")
print(s.minDepthIterative(t3), "====\n")
print(s.minDepthIterative(t4), "====\n")
print(s.minDepthIterative(t5), "====\n")