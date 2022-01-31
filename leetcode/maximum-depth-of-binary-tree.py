from helpers2 import TreeNode, create_tree

class Solution(object):
    def maxDepth(self, root: TreeNode, depth:int = 0) -> int:
        if not root:
            return depth
        else:
            return max(self.maxDepth(root.left, depth + 1), \
                       self.maxDepth(root.right, depth + 1))

    def maxDepthIterative(self, root: TreeNode) -> int:
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
t = create_tree([3, 9, 20, None, None, 15, 7])
t2 = create_tree(range(64))

t3 = TreeNode(0)
curr = t3
for i in range(1,10):
    curr.right = TreeNode(i)
    curr = curr.right

assert s.maxDepth(t) == 3
assert s.maxDepthIterative(t) == 3
assert s.maxDepth(t2) == 7
assert s.maxDepthIterative(t2) == 7
assert s.maxDepth(t3) == 10
assert s.maxDepthIterative(t3) == 10
