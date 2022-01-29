from helpers import TreeNode, listToTree

class Solution(object):
    def maxDepth(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return depth
        else:
            return max(self.maxDepth(root.left, depth + 1), \
                       self.maxDepth(root.right, depth + 1))

    def maxDepthIterative(self, root):
        if not root:
            return 0

        nodes = [(1, root)]
        maxDepth = 1

        while nodes:
            depth, node = nodes.pop(0)
            if depth > maxDepth:
                maxDepth = depth
            if node.left:
                nodes.append((depth + 1, node.left))
            if node.right:
                nodes.append((depth + 1, node.right))

        return maxDepth

s = Solution()
t = listToTree([3, 9, 20, None, None, 15, 7])
print(s.maxDepthIterative(t))